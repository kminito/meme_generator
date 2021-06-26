from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import docx


class DocxImporter(IngestorInterface):
    "Helper module to read Docx file and return list of quote models"

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str):
        print("DocxImporter")
        if not cls.can_ingest(cls, path):
            raise Exception('Connot Ingest Exception')

        quotes = []

        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                body = parse[0].strip().strip('"')
                author = parse[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
