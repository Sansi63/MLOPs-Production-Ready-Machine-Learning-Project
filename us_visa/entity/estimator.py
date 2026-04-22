import sys
from pandas import DataFrame

from us_visa.exception import USvisaException
from us_visa.logger import logging

from sklearn.pipeline import Pipeline

class TargetValueMapping:
    def __init__(self):
        self.Denied=1
        self.Certified=0
    
    def _asdict(self):
        return self.__dict__
    def reverse_mapping(self):
        mapping_response=self._asdict()
        return dict(zip(mapping_response.values(),mapping_response.keys()))