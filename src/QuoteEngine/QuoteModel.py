class QuoteModel:
    """Encapsulate the body and author
    
    @Param:
        body: str
            The quote to process
        author: str
            The author's name
    """
    def __init__(self, body, author):
        self.author = author.strip()
        self.body = body.strip()

    def __repr__(self):
        return "{0} from {1}".format(self.body, self.author)
