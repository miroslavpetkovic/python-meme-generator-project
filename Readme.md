# Meme generator

This project is about to Meme Generator.You Can generate meme using image link / path.

### MemeEngine

#### Class name:
This module includes the following classes:

  * ```MemeEngine```: resize image and draw text on image
 
#### General description
The main goal of this class to resize image if not in format. Sraw text and author name on image with random location.After succesfully complete these operation save that image.

#### module's dependencies
Module consumes the following libraries: 
```
Pillow
```
Also, the standard library module: 
```
os
random
```
#### Examples

```
meme = MemeEngine(dir_path)

# generate image with text
make_meme(self, img_path, text, author, width=500):

```

### Quote Engine

#### Class name: 
This module includes the following classes:

 * ```QuoteModel```: stores the quote and author.
 * ```ImporterInterface```: abstract class for the different importers with two attributes: ``can_ingest`` to determine which extensions files can parse and ``parse`` to parse the allowed file and output a list of ``QuoteModel``.
 * ```CSVImporter```: importer class for csv files
 * ```DocxImporter```: importer class for docx files
 * ```PDFImporter```: importer class for PDF files
 * ```TXTImporter```: importer class for txt files
 * ```Importer```: importer class with a parse method that selects the right importer for each of the allowed extensions
 

#### General description
The main goal of this class is to estore quotes and corresponging authors into a class (```QuoteModel```) and provide the required classes to ingest quotes from different file extensions.

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

#### examples
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

### Module 
```app.py``` : This module for flask web app for meme generator.
#### General description
app.py is a flask web app of meme generator. which contains these routes.
 * ``` GET -> / ``` : Random pick a photo and Quote from static our data folder.Generater meme with that **random** photo and Quote.
 * ``` GET -> /create ```: It's form page where we collect image_link, Quote, Author name through input form from User.
 * ``` POST -> /create ```: This route about to generate Meme with the help of the data which is provided by the user;


#### module's dependencies
Module consumes the following libraries: 
```
Flask
MemeEngine
QuoteEngine
```
Also, the standard library module: 
```
os
request
random
```
### Module 
```meme.py``` : This module for meme generator using terminal/cmd.
#### General description
```meme.py``` for generate meme using command line.When run this file using python3 we sends argument --path ,---body, --author.


#### module's dependencies
Module consumes the following libraries: 
```
MemeEngine
QuoteEngine
```
Also, the standard library module: 
```
os
random
```

#### Example 

```
python meme.py --path "./tmp/Lagotto-Romangolo-Tongue-Out.jpg" --body "Nice picture" --author "Miroslav"
```

## Installation
```
pip3 install -m requirement.txt
```

## How to Run

#### Generate meme from terminal
```
# to generate a meme with a random quote:
python meme.py --path path_to_image --body "message" --author "author"
```
#### Generate meme from web app

...\meme-generator-project\src>python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
