from typing import List

from .ImportInterface import ImportInterface
from .QuoteModel import QuoteModel
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .TXTImporter import TXTImporter
from .PDFImporter import PDFImporter


class Importer(ImportInterface):
    """The main Importer. We make sure we assign the various ingestors the appropriate files
    for processing.
    """
    importers = [DocxImporter, CSVImporter, PDFImporter, TXTImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Control the import process. It determine which ingest object should be called to process
        a file base on the file's extension.

        @param:
            path: str
                path to the file to process
        @return:
            A list of quotemodel object containing the processed text and author
        """
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
