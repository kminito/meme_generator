from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel
"""Module that declares abstract base class giving interface."""
class IngestorInterface(ABC):
    """
    Abstract base class for actual Ingestr classes for diffent types of files.

    Each child class will actually ingest the files and return desired data.
    """

    allowed_extensions = []

    def can_ingest(cls, path) -> bool:
        """Check whether path(file) is appliable for each ingester classes."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstractmethod for parse each type of files."""
        pass
