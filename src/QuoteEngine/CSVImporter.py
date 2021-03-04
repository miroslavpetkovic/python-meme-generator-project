import pandas
from typing import List
from .ImportInterface import ImportInterface
from .QuoteModel import QuoteModel


class CSVImporter(ImportInterface):
    """Importer for CSV. Import CSV files and process the content.
    The CSV file has text which is arrange as body and author.
        """
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Get CSV file path and extract the content.
        @param:
            path : str
                path to the csv file
        @return:
            return list of types QuoteModel
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
