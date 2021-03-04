from typing import List
import docx

from .ImportInterface import ImportInterface
from .QuoteModel import QuoteModel


class DocxImporter(ImportInterface):
    """Importer for DOCX. Importer DOCX files and process the content.
    The DOCX file has text which is arrange as body and author.

    We use the docx library to extract the docx file content
    for processing.
    """
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Get DOCX file path and extract the content.
        @param:
            path : str
                path to the DOCX file
        @return:
            return list of types QuoteModel
            """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
