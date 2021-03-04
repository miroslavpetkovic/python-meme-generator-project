from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel


class ImportInterface(ABC):

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """ Extract extension and check if it is equal to the ingestor
        @param:
            path: str
                Path to the file
        @return:
            bool
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """This is an abstract method, so no need to implement it here
        @param:
            path : str
                path to the file
        @return:
            return list of types QuoteModel
        """
        pass
