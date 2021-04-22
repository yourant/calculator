from abc import ABC, abstractmethod
from typing import List

class Calculator(ABC):

    @classmethod
    def _methods(cls) -> List[str]:
        return [func for func in dir(cls)
                    if callable(getattr(cls, func)) and not func.startswith("__")]

    @abstractmethod
    def get_data_length(self):
        ''' read the length of data needed to select from the db
            in order to reduce the time of executing query
        '''

    @abstractmethod
    def get_data_by_id(self):
        ''' search up in db for raw data needed to be calculated
            by the category_ids of the categories then return the data
        '''

    @abstractmethod
    def get_nrows_data(self):
        ''' return data with number of rows, depends on input
        '''

    @abstractmethod
    def _get_data_checked(self):
        ''' record the details of calculation and the 
            integrity of the data 
        '''

    @abstractmethod
    def get_data_cleaned(self):
        ''' cleanning up the data such as
            filling up the null values and
            converting the discrete values
            so that it could be calculated
            a.k.a ETF
        '''

    @abstractmethod
    def get_data_fixed(self):
        ''' fixing the data if it is necessary
        '''

    @abstractmethod
    def calculate(self):
        ''' calculate what needs to be calculated
        '''
    @abstractmethod
    def _post_result_db(self):
        ''' post the result of calculation to database
        '''
