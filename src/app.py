import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeEngine import MemeEngine
from QuoteEngine import Importer
from QuoteEngine import QuoteModel

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__, static_folder=dir_path)

meme = MemeEngine(dir_path)


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for quote_file in quote_files:
        quotes.extend(Importer.parse(quote_file))

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = [images_path + x for x in os.listdir(images_path)]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    print(path)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    image_url = request.form.get('image_url')
    r = requests.get(image_url)
    tmp = dir_path+'/'+str(random.randint(0, 100000000))+'.png'
    with open(tmp, 'wb') as f:
        f.write(r.content)

    if request.form.get('body') != "" and request.form.get('author') != "":
        quote = QuoteModel(request.form.get('body'),
                           request.form.get('author'))
    else:
        quote = random.choice(quotes)
    path = meme.make_meme(tmp, quote.body, quote.author)
    # os.remove(tmp)
    print(path)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
