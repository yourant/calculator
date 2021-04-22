from battery import Battery
from typing import Any, List, Union, Tuple, Optional

class Trends(Battery):
    @property
    def trends_sql(self) -> str:
        self._trends_sql = '''
                            select * from one_three_trends
                            union all
                            select * from three_ten_trends
                            union all
                            select * from over_ten_trends
                            '''
        return self._trends_sql

    def set_trend_sql(self, category_tuple: Union[Tuple[str], str]) -> str:

        self.calculate_trend_sql = f''' select category_id, asin, ranking, date 
                                        from math_model.raw_trends_data
                                        where category_id in {category_tuple}
                                    '''
        return self.calculate_trend_sql
    
    