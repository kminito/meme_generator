class QuoteModel:
    """Represent models for Quote."""

    def __init__(self, body, author):
        """Create a new `QuoTeModel`.

        :param body: content of quote in text
        :param auter: auther of qutoe in text
        """
        self.body = body
        self.author = author

    def __repr__(self):

        return f"{self.body} - {self.author}"
