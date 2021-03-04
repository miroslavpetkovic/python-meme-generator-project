from typing import List
import subprocess
import os
import random

from .ImportInterface import ImportInterface
from .QuoteModel import QuoteModel


class PDFImporter(ImportInterface):
    """Import for PDF. Import PDF files and process the content.
    The PDF file has text which is arrange as body and author.

    We use pdftotext library to open the pdf file in a subprocess.
    This converts the pdf into a txt file, then we extract the information
    and then delete the temporary created txt file.
        """
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Get PDF file path and extract the content.
        @param:
            path : str
                path to the PDF file
        @return:
            return list of types QuoteModel
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(' - ')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
