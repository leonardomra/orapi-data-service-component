from data_module.models.dataset import Dataset
from datetime import date, datetime  # noqa: F401

class DataComplex(Dataset):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, label: str=None, file_name: str=None, date_created: datetime=None, date_modified: datetime=None, format: str=None, location: str=None):  # noqa: E501
        super().__init__(id, label, file_name, date_created, date_modified)
        self._format = format
        self._location = location
    
    @property
    def format(self) -> str:
        return self._format

    @format.setter
    def format(self, format: str):
        self._format = format

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, location: str):
        self._location = location