from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    Abstract base class for actual Ingestr classes for diffent types of files.
    Each child class will actually ingest the files and return desired data
    """
    
    allowed_extensions = []

    def can_ingest(cls, path) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass

