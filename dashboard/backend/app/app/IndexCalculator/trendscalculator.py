import math
import asyncio
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt

from logger import logger
from trends import Trends
from datetime import datetime
from calculator import Calculator
from pandas.core.frame import DataFrame
from typing import Any, List, Union, Optional
from sklearn import datasets , linear_model
from sklearn.metrics import mean_squared_error , r2_score
from sklearn.model_selection import train_test_split

pd.options.mode.chained_assignment = None


class TrendsCalculator(Trends, Calculator):
    """This is a calculator built for calculating Trends of amazon global markets,
    enter 'TrendsCalculator._methods()' to see methods it contains
    """

    def __init__(self, db="local"):
        super(TrendsCalculator, self).__init__(db=db)

    def __getitem__(self, position: int) -> Union[List[str], str]:
        pass

    def __repr__(self) -> str:
        pass

    def get_data_length(self):
        pass

    def get_data_by_id(self):
        pass

    def get_nrows_data(self):
        pass

    def _get_data_checked(self):
        pass

    def get_data_cleaned(self):
        pass

    def get_data_fixed(self):
        pass

    def calculate(self):
        pass

    def get_trends(self,df:DataFrame):
        ans = {}
        df["date"] = pd.to_datetime(df["date"]).apply(
            lambda x: (datetime.today() - x).days
        )

        df.columns = df.columns.to_series().replace({"date": "days"})
        df = df[df["days"] <= 720]
        drop_asins = (
            df.groupby("asin")
            .size()
            .sort_values()[df.groupby("asin").size().sort_values() <= 60]
        )

        df = df[~df["asin"].isin(drop_asins.index)]

        for index in range(df["category_id"].nunique()):
            current_category_id = df["category_id"].unique()[index]
            sumcoef = []
            for asin in df[df["category_id"] == current_category_id]["asin"].unique():
                try:
                    sts = sm.tsa.seasonal_decompose(
                        df[df["asin"] == f"{asin}"]['ranking'], period=30
                    )
                    X = sts.trend[sts.trend.notna()].index
                    y = sts.trend[sts.trend.notna()].values.astype("int")
                    model = linear_model.LinearRegression()
                    model.fit(np.array(X).reshape(-1, 1), y)
                    sumcoef.append(model.coef_)
                except:
                    print(f"An exception occurred with asin {asin}")

            ans[current_category_id] = np.array(sumcoef).mean()
        finans = {k: v for k, v in sorted(ans.items(), key=lambda item: item[1])}
        return finans

    def read_trends(self):
        with self.db_engine.connect() as conn:
            self.trends_sql = self.set_trend_sql()
            df = pd.read_sql(self.trends_sql, con=conn)
    def _post_result_db(self):
        pass

trendscalculator = TrendsCalculator()

if __name__ == "__main__":
    trendscalculator.calculate()