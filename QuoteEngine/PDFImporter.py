from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess
import random
import os


class PDFImporter(IngestorInterface):
    "Helper module to read PDF file and return list of quote models"

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str):
        if not cls.can_ingest(cls, path):
            raise Exception('Connot Ingest Exception')

        quotes = []

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        file_ref = open(tmp, "r")

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                new_quote = QuoteModel(parsed[0].strip().strip('"'), parsed[1].strip())
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)

        return quotes
