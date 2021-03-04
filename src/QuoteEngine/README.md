# Quote Engine

### Class name: 
This module includes the following classes:

 * ```QuoteModel```: stores the quote and author.
 * ```ImporterInterface```: abstract class for the different importers with two attributes: ``can_ingest`` to determine which extensions files can parse and ``parse`` to parse the allowed file and output a list of ``QuoteModel``.
 * ```CSVImporter```: importer class for csv files
 * ```DocxImporter```: importer class for docx files
 * ```PDFImporter```: importer class for PDF files
 * ```TXTImporter```: importer class for txt files
 * ```Importer```: importer class with a parse method that selects the right importer for each of the allowed extensions
 

### General description
The main goal of this class is to estore quotes and corresponging authors into a class (```QuoteModel``) and provide the required classes to ingest quotes from different file extensions.

### module's dependencies
Module consumes the following libraries: 
```
Flask == 1.1.2
Pillow == 8.1.0
pandas == 1.2.1
python_docx == 0.8.10
requests == 2.25.1
```
Also, the standard library module: 
```
typing
abc
subprocess
random
```

### examples
```
quote = "Hola, que tal?"
author = "Rafa"

# generate a quote class:
quotemodel = QuoteModel(quote, author)

# import quotes from docx using specific importer
docx = DocxImporter()
quotes = docx.parse("./_data/DogQuotes/DogQuotesDOCX.docx")

# import quotes from docx using generic importer
quotes = Importer().parse("./_data/DogQuotes/DogQuotesDOCX.docx")
```