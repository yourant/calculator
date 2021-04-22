from abc import ABC, abstractmethod
from sqlalchemy.sql.schema import Index
from indexcalculator import IndexCalculator
from trendscalculator import TrendsCalculator

# the proxy of all calculators, instantialize ur calculators here so that they can all be imported
# from here

uscalculator = IndexCalculator('us')
trendscalculator = TrendsCalculator()

































