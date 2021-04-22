import sqlalchemy

from abc import ABC, abstractmethod
from pandas.core.frame import DataFrame
from typing import Tuple, Union, Optional, Dict, Any, Generator
from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine


class Battery(ABC):

    db_params = {
    'db': 'mysql',
    'driver': '',
    'user': '',
    'password': '',
    'host': '',
    'schema': '',
}

    def __init__(self, db: str = "local"):
        if db == "local":
            self.db_params["user"] = "chencheng"
            self.db_params["password"] = "iKWz@4*7W55"
            self.db_params["host"] = "10.1.1.202:3306"

        elif db == "cloud":
            self.db_params["user"] = "root"
            self.db_params["password"] = "123"
            self.db_params["host"] = "121.37.218.157:3306"
            self.db_params["schema"] = "racebase"


    @staticmethod
    def set_column_types(df: DataFrame) -> dict:
        if not df:
            print("Input is empty")

        dtypedict = {}
        for column, dtype in zip(df.columns, df.dtypes):
            if "object" in str(dtype):
                dtypedict.update({column: sqlalchemy.types.NVARCHAR(length=255)})

            if "datetime" in str(dtype):
                dtypedict.update({column: sqlalchemy.types.Date()})

            if "float" in str(dtype):
                dtypedict.update({column: sqlalchemy.types.Float(precision=3, asdecimal=True)})

            if "int" in str(dtype):
                dtypedict.update({column: sqlalchemy.types.INT()})
        return dtypedict

    @staticmethod
    def db_assemble(db_params:Optional[Dict[str, str]] = None) -> str:
        db_url = f'''{db_params['db']}+{db_params['driver']}://{db_params['user']}:{db_params['password']}@{db_params['host']}'''
        db_url = (db_url + f'''/{db_params['schema']}'''
            if db_params["schema"]
            else db_url
        )
        return db_url

    @property
    def async_db_engine(self, db_params: Optional[Dict[str, str]] = None) -> Any:
        db_params = db_params or self.db_params
        self.db_params['driver'] = 'aiomysql'
        _async_db_engine_url = self.db_assemble(db_params)
        return create_async_engine(_async_db_engine_url, pool_pre_ping=True) 

    @property
    def db_engine(self, db_params:Optional[Dict[str, str]] = None) -> Any:
        db_params = db_params or self.db_params
        self.db_params['driver'] = 'pymysql'
        _db_engine_url = self.db_assemble(db_params)
        return create_engine(_db_engine_url, pool_pre_ping=True)





