from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextImporter(IngestorInterface):
    """Helper module to read text file."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str):
        """Parse txt file and list of quote models."""
        print("TextImporter Executed")
        if not cls.can_ingest(cls, path):
            raise Exception('Connot Ingest Exception')

        quotes = []

        with open(path, 'r') as f:
            for line in f:
                body = line.split("-")[0].strip().strip('"')
                author = line.split("-")[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
