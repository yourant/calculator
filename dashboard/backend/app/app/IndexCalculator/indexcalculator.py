import math
import asyncio
import numpy as np
import pandas as pd
from index import Index
from logger import logger
from sqlalchemy import text
from datetime import datetime
from calculator import Calculator
from pandas.core.frame import DataFrame
from typing import Any, List, Union, Optional
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

pd.options.mode.chained_assignment = None


class IndexCalculator(Index, Calculator):
    """This is a calculator built for calculating indexes of amazon global markets,
    use 'IndexCalculator._methods()' to see methods it contains
    """

    db_columns_comments = {
        "category_id": "亚马逊品类ID",
        "maincategory": "亚马逊品类名称",
        "site": "亚马逊站点",
        "amv": "品类市场容量(当地货币)",
        "cii": "竞争激烈指数：该指数越高则说明当前品类竞争越为激烈",
        "cci": "行业集中指数：该指数越高则说明当前品类寡头垄断程度越严重",
        "pqi": "商品品质指数：该指数越高则说明当前品类下的商品平均品质越高",
        "nvpi": "新品友好指数：该指数越高则说明当前品类下新品市场份额占比越高",
        "cvr": "中国卖家销售额占比: 该比例计算当前品类下中国卖家的销售额占比",
        "avr": "亚马逊自营销售额占比: 该比例结算当前品类下亚马逊自营的销售额占比",
        "asr": "亚马逊自营比例：该比例越高则说明当前品类下卖家为亚马逊自营比列越高",
        "csr": "中国卖家比列：该比例越高则说明当前品类下商品为中国卖家所售比例越高",
        "remark_used": "计算使用的数据的标识日期，取最近一次有效标识",
        "created_at": "计算完成并存入数据库的日期",
    }


    def __init__(self, site: str, db: str="local"):
        super(IndexCalculator, self).__init__(db=db)
        self.site = site.lower()
        self._nowtime = datetime.today().strftime("%Y-%m-%d")

    def __getitem__(self, position: int) -> Union[List[str], str]:
        return self._remarks[position]

    def __repr__(self) -> str:
        return f""" An index calculator of the {self.site} site
                methods: {[', '.join(i for i in IndexCalculator._methods())]} \n
                """

    @property
    async def remarks(self) -> DataFrame:
        ''' return most recent five remarks ordered by date
        '''
        self.remark_sql = self.set_remark_sql(self.site)
        async with self.async_db_engine.connect() as conn:
            result = await conn.execute(text(self.remark_sql))
            self._remarks = pd.DataFrame(result.fetchall(), columns=result.keys()).iloc[:5,:]
        return self._remarks

    @property
    async def remark(self) -> str:
        """ return an remark that is available to use, which means \n
        the remark has been existing in the db for more than two days
        """
        if (
            pd.to_datetime(self._nowtime)
            -
            pd.to_datetime(
                (await self.remarks).iloc[0][0][-10:]
            )
        ).days > 2:
            self._remark = (await self.remarks).iloc[0][0]
        else:
            self._remark = (await self.remarks).iloc[1][0]
        return self._remark

    @property
    async def last_update_date(self) -> datetime:
        ''' return a pandas Datetime object indicates the remark
            being used in the last update, then compare it to the newest remark
            to avoid repeated calculation
        '''

        self.last_sql = self.set_last_sql(self.site)
        async with self.async_db_engine.connect() as conn:
            result = await conn.execute(text(self.last_sql))
            self._last_update_date = pd.to_datetime(pd.DataFrame(result.fetchall(), columns=result.keys()).iloc[0][0])
        return self._last_update_date

    @property
    async def is_data_ready(self) -> bool:
        ''' _pre_update_date shows the date of newest remark available
            and compare it to the last_update_date, and return a boolean
            value indicates wether the remark is never used in the previous updates.
        '''

        self._pre_update_date = (await self.remark)[-10:]
        self._pre_update_date = pd.to_datetime(self._pre_update_date)
        self._last_update_date = await self.last_update_date
        self._is_data_ready =  self._last_update_date < self._pre_update_date
        return self._is_data_ready

    async def get_data_length(self, remark: str) -> int:
        ''' search of the length of the data that would be 
            retrived in the upcoming queries, so that the time 
            of executing those queries would be reduced as much as possible.
        '''

        async with self.async_db_engine.connect() as conn:
            self.data_len_sql = self.set_length_sql(remark=remark)
            result = await conn.execute(text(self.data_len_sql))
            data_len = int(result.fetchall()[0][0]) or 0
        return data_len

    async def get_data_by_id(
        self,
        *,
        category_id: Union[tuple, str],
        remark: Optional[str] = None,
        getindexes: bool = False,
    ) -> DataFrame:
        """accept one single category_id in str or couples of categories_ids in tuple, \n
        would return either the original data stored inside the database or \n
        the indexes calculated based on the original data if the parameter 'getindexes' is set to be True
        """

        if remark:
            self._remark = remark

        if isinstance(category_id, tuple) and len(category_id) > 1:
            self.id_sql = self.set_id_sql(category_tuple=category_id, remark=self._remark)
        elif isinstance(category_id, str):
            category_id = f"""('{category_id}')"""
            self.id_sql = self.set_id_sql(category_tuple=category_id, remark=self._remark)
        else:
            raise TypeError("Input type has to be either tuple or str")

        async with self.async_db_engine.connect() as conn:
            result = await conn.execute(text(self.id_sql))
            self.data = pd.DataFrame(result.fetchall(), columns=result.keys())

        if getindexes:
            try:
                self.data = await self.calculate(df=self.get_data_cleaned(df=self.data), date_check=False, remark=self._remark)
                print('passing parameter remark', self._remark)
            except:
                logger.info('an error occured when calculating indexes')
            finally:
                return self.data
        return self.data

    async def get_nrows_data(
        self,
        *,
        remark: Optional[str] = None,
        rows: Optional[int] = None,
        clean: bool = True,
    ) -> DataFrame:
        """the newest available remark will be used without specific remark assgiend to the method,
        the number of rows the newest remark will be used without specific rows assigned to the method.
        """
        if remark or rows:
            if remark:
                self._remark = remark
                self.rows = await self.get_data_length(remark=self._remark)
                if rows:
                    self.rows = rows
            if rows:
                self.rows = rows
                self._remark = await self.remark
        else:
            self._remark = await self.remark
            self.rows = await self.get_data_length(remark=self._remark)

        df = pd.DataFrame()

        if self.rows <= 2000000:
            logger.info(f"正在查询{self.rows}行{(self._remark)[-5:]}日{self.site.upper()}站数据")
            pages = [0, self.rows]
            interval = self.rows
            self.data_sql = self.set_data_sql(
                remark=self._remark, interval=interval, pages=pages, index=1
            )

            async with self.async_db_engine.connect() as conn:
                result = await conn.execute(text(self.data_sql))
                _partial_df = pd.DataFrame(result.fetchall(), columns=result.keys())
                df = df.append(_partial_df)

        else:
            interval = int(self.rows / 2)
            pages = list()
            for page in range(2):
                pages.append(page * interval)
            pages.append(self.rows)
            logger.info(
                f"正在查询{self.rows}行{(self._remark)[-5:]}日{self.site.upper()}站数据，数据量太大, 将数据分为{pages}进行分页查询"
            )
            initial = 1
            while initial < len(pages):
                self.data_sql = self.set_data_sql(
                    remark = self._remark,
                    interval = self.interval,
                    pages = pages,
                    index = self.initial,
                )
                async with self.async_db_engine.connect() as conn:
                    result = await conn.execute(text(self.data_sql))
                    _partial_df = pd.DataFrame(result.fetchall(), columns=result.keys())
                    df = df.append(_partial_df)
                self.initial += 1

        logger.info(f"已完成{self.rows}行查询")

        if clean:
            self.data = self.get_data_cleaned(df=df)
        else:
            self.data = df
        return self.data

    def _get_data_checked(self, df: pd.DataFrame) -> DataFrame:
        """this method should not be called directly from ousdie"""

        self.data = df
        categories = self.data["category_id"].nunique()
        valid_dates_rate = round((1-(self.data["release_date"].isnull().sum()
                    + (self.data["release_date"] == "0000-00-00").sum())
                    / (self.data.shape[0]))*100,3)
        
        valid_rows = (self.data["mrevenue"].fillna(0).astype(
                        "int", errors="ignore")>=1).sum()
        self.data["ranking"] = self.data["ranking"].fillna(0).astype("int")
        valid_cii = (
            min(
                round((
                        self.data[self.data["ranking"].fillna(0).astype("int") <= 8]
                        .groupby("category_id")
                        .size()/8).mean(),3,
                ),
                round((
                        self.data[(self.data["ranking"] >= 1)]
                        .groupby("category_id")
                        .size()
                        /self.data.groupby("category_id")["ranking"].max()).mean(),3,
                ),
            )
        ) * 100

        valid_asin_ratio = round((1 - (valid_rows/self.data.shape[0]))*100, 3)

        if self.data.shape[0] >= 200000 and valid_cii <= 87.5:
            self.data = self.get_data_fixed(df=self.data)

        logger.info(
            f"""已完成{self.data.shape[0]}行{self.site.upper()}站数据查询,\n
                共{categories}个品类\n
                其中有{valid_rows}行有效,\n
                有效比例为: {valid_asin_ratio}%,\n
                有效cii占比：{valid_cii}%,\n
                有效日期占比：{valid_dates_rate}%,\n
             """
        )
        return df

    def get_data_cleaned(self, df: pd.DataFrame) -> Any:
        """as the name suggests, this method is for cleanning up the data
        and get it prepared before the data getting calculated.
        for each column of the data, if it is supposed of the type int we convert it to float first
        and then fill nan values with the mean of the column and finally conver it to int
        for columns of the type float, we do the similar thing except round the number to one digit.
        """
        df = self._get_data_checked(df=df)

        for column in df.columns:
            if column == "ranking":
                df[f"{column}"].fillna(0, inplace=True)

            elif self.cols_dtypes[f"{column}"] == "int":
                df[f"{column}"] = (
                    df[f"{column}"]
                    .fillna(pd.to_numeric(df[f"{column}"], errors="coerce").mean())
                    .astype("float")
                    .apply(lambda x: int(x))
                )
            elif self.cols_dtypes[f"{column}"] == "float":
                df[f"{column}"] = (
                    df[f"{column}"]
                    .fillna(pd.to_numeric(df[f"{column}"], errors="coerce").mean())
                    .astype("float")
                    .apply(lambda x: round(x, 1))
                )
            df[f"{column}"] = df[f"{column}"].astype(
                self.cols_dtypes[f"{column}"], errors="ignore")

        # we don't calculate categories which more than half of its all asins have no mrevenue
        valid_cat_num = df[df["mrevenue"] > 1].groupby("category_id").size()
        total_cat_num = df.groupby("category_id").size()
        for category in (set(df['category_id'])-set(valid_cat_num.index)):
            valid_cat_num[f'{category}'] = 0
        _ic = (valid_cat_num / total_cat_num).apply(lambda x: x <= 0.5)
        self.invalid_categories = _ic[_ic].index
        df = df[~df["category_id"].isin(self.invalid_categories)]
        dropped_size = len(_ic[_ic].index)
        try:
            logger.info(f"dropped :{dropped_size} categories")
        except:
            print(f"dropped :{dropped_size} categories")

        df.loc[
            (df["release_date"].isna()) | (df["release_date"] == "0000-00-00"),
            "release_date",] = self._nowtime

        df.loc[
            df["release_date"].str.split("/").apply(lambda x: len(x) == 3),
            "release_date",] = pd.to_datetime(
            df[df["release_date"].str.split("/").apply(lambda x: len(x) == 3)]["release_date"],
            format="%m/%d/%Y",).dt.date

        df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

        df["days_since_released"] = (
            df["release_date"]
            .apply(lambda x: pd.to_datetime(self._nowtime) - x)
            .dt.days.fillna(0)
            .astype(int)
        )
        df.drop(columns="release_date", inplace=True)
        self.data = df
        return self.data

    def get_data_fixed(self, df: pd.DataFrame, ranknum: int = 9) -> DataFrame:
        """fixing the rows missing revenue and fulfilled with Linear Regression
        adjusting the range of fixing with parameter ranknum, notice that
        ranknum = 9 means fixing the asins with rank from 1 to 8.
        """

        originalrows = df.shape[0]
        fullrank = list(range(1, ranknum))

        for cat_id in iter(df["category_id"].unique()):
            X = df.loc[df["category_id"] == cat_id, ["ranking"]].values
            y = df.loc[df["category_id"] == cat_id, "mrevenue"].values

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.3, random_state=0
            )
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)

            currentrank = list(
                df[(df["category_id"] == cat_id) & (df["ranking"] <= 8)][
                    "ranking"
                ].values
            )

            MissedRank = list(set(fullrank) - set(currentrank))

            res, ans = [], []
            for rank in MissedRank:
                res.append(abs(int(regressor.predict([[rank]])[0])))

            for rank, predictedvalue in zip(MissedRank, res):
                ans.append((rank, predictedvalue))

            for pairs in range(len(ans)):
                self.fixedrow = {}
                for i, j in zip(
                    df.columns, df[df["category_id"] == cat_id].iloc[0, :].values
                ):
                    self.fixedrow[f"{i}"] = j
                self.fixedrow["ranking"] = ans[pairs][0]
                self.fixedrow["mrevenue"] = ans[pairs][1]
                self.fixedrow["asin"] = "Fixed"
                df = df.append(self.fixedrow, ignore_index=True)
        try:
            logger.info(f"已完成数据填补工作，通过线性回归修补了{len(df) - originalrows}行数据,现在开始指数计算")
        except:
            print(f"已完成数据填补工作，通过线性回归修补了{len(df) - originalrows}行数据,现在开始指数计算")
        self.data = df

        return self.data

    def _getcii(self, df: pd.DataFrame) -> DataFrame:
        """Competitive Intensity Index"""
        self.cii = (
            (df.groupby("category_id").mrevenue.apply(
                lambda x: int(
                    (1-((((((((x / x.sum()) * 100)
                        -(((x / x.sum()) * 100).sum()
                            / x.size))** 2).sum())
                            /(x.size - 1))** 0.5)
                        /((((x.size * (100 ** 2)) - (100 ** 2))
                    /(x.size ** 2 - x.size))** 0.5)))* 100)))
            .to_frame()
            .reset_index()
            .rename({"mrevenue": "cii"}, axis="columns"))
        return self.cii

    def _getcci(self, df: pd.DataFrame) -> DataFrame:
        """Industrial Concentration Index"""
        self.cci = (
            (
                df.sort_values(by=["mrevenue"], ascending=False)
                .groupby("category_id")
                .head(8)
                .loc[:, ["category_id", "mrevenue"]]
                .groupby("category_id")["mrevenue"]
                .sum()
                / df.sort_values(by=["mrevenue"], ascending=False)
                .groupby("category_id")["mrevenue"]
                .sum()
            )
            .apply(lambda x: int(x * 100))
            .to_frame()
            .reset_index()
            .rename({"mrevenue": "cci"}, axis="columns")
        )
        return self.cci

    def _getnvpi(self, df: pd.DataFrame) -> DataFrame:
        """Newly validated product index"""
        _unproccessed = (
            df.query("days_since_released <= 90")
            .groupby("category_id")
            .agg({"mrevenue": np.sum})
        )
        _proccessed = (df.groupby("category_id").agg({"mrevenue": np.sum}))[
            ~(df.groupby("category_id").agg({"mrevenue": np.sum})).index.isin(
                (
                    df.query("days_since_released <= 90")
                    .groupby("category_id")
                    .agg({"mrevenue": np.sum})
                ).index
            )
        ]
        _proccessed["mrevenue"] = 0
        self.nvpi = (
            (
            (_unproccessed.append(_proccessed))
            / (df.groupby("category_id").agg({"mrevenue": np.sum}))
            )["mrevenue"]
            .apply(lambda x: int(x * 100))
            .to_frame()
            .reset_index()
            .rename({"mrevenue": "nvpi"}, axis="columns")
        )
        self.nvpi["nvpi"] = (
            self.nvpi["nvpi"].apply(lambda x: (1 / (1 + math.exp(-x))) * 100).astype(int)
        )
        return self.nvpi

    def _getpqi(self, df: pd.DataFrame) -> DataFrame:
        """Product Quality Index"""
        self.pqi = (
            (
                (
                    df.query("rating <= 4.6").groupby("category_id").ranking.count()
                    / df.groupby("category_id").ranking.count()
                )
                * 100
            )
            .fillna(0)
            .astype("int")
            .to_frame()
            .reset_index()
            .rename({"ranking": "pqi"}, axis="columns")
        )
        return self.pqi

    async def get_indexes(
        self,
        df: Optional[DataFrame] = None,
        postdb: bool = False,
        remark: str = None,
        date_check: bool = True,
    ) -> DataFrame:
        ''' calculating the four indexes based on given parameters,
            df is the 'raw data' which will be used to calculate indexes,
            it would be a pandas DataFrame with columns written in 'index.py' col_types
            if remark is given it would use the given remark over the default remark
            if date_check is set to be false it would execute the calculation despite it 
            could possibly produce a existing result
        '''

        if remark:
            self._remark = remark
        if date_check:
            assert (await self.is_data_ready), "data is already up-to-date"
        self.data = pd.DataFrame(df)

        if self.data.empty:
            self.data = await self.get_nrows_data()

        if ("days_since_released") in self.data.columns.values:
            assert (
                self.data["days_since_released"].dtype == "int" 
                or self.data["days_since_released"].dtype == "int64" 
            ), """ the column 'days_since_released' should be of type int"""
            for column in self.data.columns.difference(("days_since_released",)):
                assert (
                    self.cols_dtypes[f"{column}"] == self.data[f"{column}"].dtype
                ), f"""{column} is not of type {self.cols_dtypes[f'{column}']}"""
        else:
            self.data = await self.get_data_cleaned(df=self.data)

        logger.info(f"calculating indexes using {self._remark}")

        self.data = (
            self.data.drop_duplicates("category_id")
            .merge(self._getcii(df=self.data), on="category_id")
            .merge(self._getcci(df=self.data), on="category_id")
            .merge(self._getpqi(df=self.data), on="category_id")
            .merge(self._getnvpi(df=self.data), on="category_id")
            .loc[:, ["category_id", "maincategory", "amv", "cii", "cci", "pqi", "nvpi"]]
        )
        self.data["site"] = self.site
        logger.info("计算完成")

        if postdb:
            self._post_result_db(result=await self.calculate(df=self.data))

        return self.data

    async def calculate(
        self, 
        df: Optional[DataFrame] = None,
        postdb: bool = False,
        date_check: bool = True,
        remark: str = None
    ) -> DataFrame:
        ''' the entrance of the program, by default it would 
            check if the four indexes are in the DataFrame, if not
            it would execute the previous get_indexes method and then 
            search for extra indexes such as csr and asr.
        '''
        if date_check:
            assert (await self.is_data_ready), "data already is up-to-date"
        if remark:
            self._remark = remark
        logger.info("开始全品类查询与计算")
        self.data = pd.DataFrame(df)
        if ("cii" and "cci" and "pqi" and "nvpi") not in self.data.columns:
            self.data = await self.get_indexes(df=self.data, remark=self._remark)

        category_tuple = (
            tuple(self.data["category_id"].unique())
            if len(self.data["category_id"].unique()) > 1
            else f"""('{self.data['category_id'].unique()[0]}')"""
        )

        ms_sql = self.set_ms_sql(remark=self._remark, category_tuple=category_tuple)
        sr_sql = self.set_sr_sql(category_tuple=category_tuple)

        async with self.async_db_engine.connect() as conn:
            msresult = await conn.execute(text(ms_sql))
            csrresult = await conn.execute(text(sr_sql))
            ms_data = pd.DataFrame(msresult.fetchall(), columns=msresult.keys())
            csr_data = pd.DataFrame(csrresult.fetchall(), columns=csrresult.keys())

        self.data = pd.merge(self.data, ms_data, how="left", on="category_id").merge(
            csr_data
        )
        if postdb:
            self._post_result_db(result=self.data)
        return self.data

    def _post_result_db(
        self,
        *,
        result: pd.DataFrame,
        table_name: Optional[str] = None,
        method: str = "append",
    ) -> None:
        """post result of calculation with a default method of appending"""
        if self._is_data_ready:
            self.result = result
            self.table_name = table_name or f"categories_index_{self.site}"
            self.result = self.result.loc[
                :,
                [
                    "category_id",
                    "maincategory",
                    "site",
                    "amv",
                    "cii",
                    "cci",
                    "pqi",
                    "nvpi",
                    "cvr",
                    "avr",
                    "asr",
                    "csr",
                ],
            ]
            self.result.drop_duplicates("category_id", inplace=True)
            self.result["remark_used"] = pd.to_datetime(
                self._remark[-10:], utc=False
            ).date()
            self.result["remark_used"] = pd.to_datetime(self.result["remark_used"])
            self.result["created_at"] = pd.to_datetime(self._nowtime, utc=False).date()
            self.result["created_at"] = pd.to_datetime(self.result["created_at"])
            self.outputdict = self.set_column_types(self.result)

            with self.db_engine.connect() as conn:
                self.result.to_sql(
                    f"{self.table_name}",
                    if_exists = method,
                    con = conn,
                    method = "multi",
                    index = False,
                    dtype = self.outputdict,
                )
                if method == "replace":
                    conn.execute(
                        f"""alter table math_model.{self.table_name} add primary key(category_id, remark_used);"""
                    )
                for column, dtype in self.outputdict.items():
                    set_comment = f"""alter table math_model.{self.table_name} modify {column} {dtype} comment '{self.db_columns_comments[column]}';"""
                    conn.execute(set_comment)
            logger.info(f"已存入 math_model.{self.table_name}")
        else:
            logger.info(f"{self._remark} is nearer than {self._last_update_date}")


async def main() -> Optional[DataFrame]:
    calculators = [IndexCalculator(f"{country}") for country in countries]
    for calculator in calculators:
        logger.info(f"now calculating {calculator.site} site data")
        await calculator.calculate(postdb=True)
        logger.info(f"{calculator.site} index calculation finished)")
    logger.info("All site index calculation finished")

countries = ["us", "uk", "de", "it", "jp", "fr", "es"]

if __name__ == "__main__":
    logger.info("start running indexes calculation of all sites")
    asyncio.run(main())

# uscalculator = build_calculator(IndexCalculator('us'))
uscalculator = IndexCalculator('us')
