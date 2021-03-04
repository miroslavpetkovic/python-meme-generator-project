from typing import List

from .ImportInterface import ImportInterface
from .QuoteModel import QuoteModel


class TXTImporter(ImportInterface):
    """Importer for TXT. Import TXT files and process the content.
    The TXT file has text which is arrange as body and author.
        """
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Get TXT file path and extract the content.
        @param:
            path : str
                path to the TXT file
        @return:
            return list of types QuoteModel
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, 'r') as f:
            for line in f.readlines():
                body, author = line.split(" - ")
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
