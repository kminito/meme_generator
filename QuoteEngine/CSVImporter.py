from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import pandas


class CSVImporter(IngestorInterface):
    "Helper module to read CSV file and return list of quote models"

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path:str):
        if not cls.can_ingest(cls,path):
            raise Exception('Connot Ingest Exception')

        quotes = []

        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes