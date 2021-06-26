from QuoteEngine.QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVImporter import CSVImporter
from .DocxImporter import DocxImporter
from typing import List


class Ingestor(IngestorInterface):

    ingestors = [CSVImporter, DocxImporter]    
    
    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            # print(ingestor)
            # print(path)
            # print(ingestor.can_ingest(ingestor,path))
            if ingestor.can_ingest(ingestor,path):
                return ingestor.parse(path)