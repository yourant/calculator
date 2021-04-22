import pandas as pd
from battery import Battery
from sqlalchemy import text
from typing import Tuple, Union

class Index(Battery):

    cols_dtypes = {
        "maincategory": "object",
        "category_id": "object",
        "amv": "int",
        "asin": "object",
        "ranking": "int",
        "rating": "float",
        "mrevenue": "int",
        "release_date": "object",
    }

    def set_length_sql(self, remark: str) -> str:
        ''' take remark as an input and look up in the db 
            to find the total number of rows the data 
            satisfies the remark condition continas 
        '''

        self.data_len_sql = f'''with a as (select r.category_id as category_id,
                                    c.top_data as top_data,
                                    c.amazon_market_share_money as amv
                                from amazon_analysis.category_report r
                                join amazon_analysis.category_report_result_content c
                                on r.result_id = c.id
                                where remark = '{remark}' and r.status = '完成'),
                                b as (select  top_data->>'$[*].ASIN' as asin from a)
                                select sum(JSON_LENGTH(asin)) from b
                            '''
        return self.data_len_sql

    def set_last_sql(self, site: str) -> str:
        ''' search for the remark used in last update of the  table
            and then use it to compare newest remark available in the db
            so that no repeated calculation would occur
        '''

        self.last_sql = f'''select max(remark_used) as remark_used 
                            from math_model.categories_index_{site}
                         '''
        return self.last_sql

    def set_remark_sql(self, site: str) -> str:
        ''' the IndexCalculator would require a 'site' input 
            for it to be instantiated, then it would look up remarks 
            avaiable for the site via this method
        '''

        self.remark_sql = f''' select distinct remark from amazon_analysis.category_report where remark like 
                            'all_categories_{site}_202%%-%%%%-%%%%' order by created_at desc limit 10
                           '''
        return self.remark_sql

    def set_id_sql(self, remark: str, category_tuple: Union[Tuple[str], str]) -> str:
        ''' This query would return data under the condition of given remark and category_id
            it would offer extra help when the indexes of some categories seem to be wrong 
            and you would like to know why by looking at the raw data of those categories.
        '''

        self.id_sql = f'''select context_name as maincategory,
                        r.category_id,
                        rc.amazon_market_share_money  as amv,
                        json_unquote(json_extract(top_data, concat('$[', i.idx, ']."ASIN"'))) as asin,
                        json_unquote(json_extract(top_data, concat('$[', i.idx, ']."#"'))) as ranking,
                        json_unquote(json_extract(top_data, concat('$[', i.idx, ']."星级"'))) as rating,
                        json_unquote(json_extract(top_data, concat('$[', i.idx, ']."月收入"'))) as mrevenue,
                        json_unquote(json_extract(top_data, concat('$[', i.idx, ']."first_date"'))) as release_date
                    from amazon_analysis.category_report r
                    join amazon_analysis.category_report_result_content rc on r.result_id = rc.id
                    join mws_data.category_all c on c.id = r.category_id
                    join amazon_analysis.idx i
                    where remark = '{remark}' and r.status='完成' and category_ID In {category_tuple}
                '''
        return self.id_sql

    def set_data_sql(
        self, remark: str, interval: int=200, pages: list=[0, 200], index: int=1
    ) -> str:
        ''' this query is used for retriving large amount of data, by setting,
            once data goes beyond 2million rows, it would split the query into different stages
            and then looping through them.
        '''

        self.data_sql = f'''select context_name as maincategory,
                                r.category_id,
                                rc.amazon_market_share_money as amv,
                                json_unquote(json_extract(top_data, concat('$[', i.idx, ']."ASIN"'))) as asin,
                                json_unquote(json_extract(top_data, concat('$[', i.idx, ']."#"'))) as ranking,
                                json_unquote(json_extract(top_data, concat('$[', i.idx, ']."星级"'))) as rating,
                                json_unquote(json_extract(top_data, concat('$[', i.idx, ']."月收入"'))) as mrevenue,
                                json_unquote(json_extract(top_data, concat('$[', i.idx, ']."first_date"'))) as release_date
                            from amazon_analysis.category_report r
                            join amazon_analysis.category_report_result_content rc on r.result_id = rc.id
                            join mws_data.category_all c on c.id = r.category_id
                            join amazon_analysis.idx i
                            where remark = '{remark}' and r.status = '完成'            
                            limit  {interval}
                            offset {pages[index-1]+1}
                        '''
        return self.data_sql

    def set_ms_sql(self, remark: str, category_tuple: Union[Tuple[str], str]) -> str:
        ''' get the ratio of market share that are either chinese or amazon in market share of all sellers'''

        self.ms_sql = f'''select category_id,
                            round(sum(if(business_address like '%%CN%%',mrevenue,0))/sum(mrevenue),2) as cvr,
                            round(sum(if(seller_name like 'amazon.com' ,mrevenue,0))/sum(mrevenue),2) as avr
                        from
                            (select cs.asin,cs.mrevenue,ss.business_address, ss.seller_name,category_id
                                from
                                    (select 
                                        distinct json_unquote(json_extract(c.top_data, concat('$[', idx.idx, ']."ASIN"'))) as asin,
                                        json_unquote(json_extract(c.top_data, concat('$[', idx.idx, ']."月收入"'))) as mrevenue,
                                        r.category_id
                                        from amazon_analysis.category_report r
                                        join amazon_analysis.category_report_result_content c
                                        on r.result_id = c.id
                                        join amazon_analysis.idx idx
                                        where remark = '{remark}' and status = '完成'
                                        and category_id IN {category_tuple}
                                        having asin is not null                              
                            )cs 
                        join amazon_ba.asin_seller s on cs.asin = s.asin
                        join amazon_ba.seller ss on ss.seller_id = s.seller_id
                        where s.is_buy_box = true)t2
                        group by category_id
                    '''
        return self.ms_sql

    def set_sr_sql(self, category_tuple: Union[Tuple[str], str]) -> str:
        '''get the ratio of sellers that are either chinese or amazon in proportion to all sellers'''

        self.sr_sql = f'''select category_id,round(ifnull(amazonseller/asin_count,0),3) as asr,
                                        round(ifnull(cn_seller/asin_count,0),3) as csr
                            from (select cs.category_id,
                                    count(distinct cs.asin)                                            as asin_count,
                                    count(distinct if(ss.business_address like '%%CN%%', s.asin, null))  as cn_seller,
                                    count(distinct if(ss.seller_name like 'amazon.com', s.asin, null)) as amazonseller
                            from mws_data.report_asins cs
                            join amazon_ba.asin_seller s on cs.asin = s.asin
                            join amazon_ba.seller ss on ss.seller_id = s.seller_id and ss.site = 'us'
                            where s.is_buy_box = true and cs.category_id IN {category_tuple}
                            group by category_id)t1
                        '''
        return self.sr_sql