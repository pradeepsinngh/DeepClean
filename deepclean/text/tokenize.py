import re
from bs4 import BeautifulSoup
from deepclean.main import Data

class Tokenize(Data):
    """
    Tokenize is a sub-class  of Data Class which implements various methods
    for tokinizing text data.

    ...

    Attributes
    ----------


    """

    def __inti__(self):
        pass

    def split_by_whitespace(self, text):
        """
        Split the given text wherever whitespace exist.

        Parameters
        ----------
        text : str
            list of sentences/ words / paragraph - text data

        Retunrs
        ------
        words : str
                list of words splitted at whitespace
        """
        words = text.split()
        return words

    def split_by_words(self, text):
        """
        Splits the given text into words.

        Parameters
        ----------
        text : str
            list of sentences/ words / paragraph - text data

        Retunrs
        ------
        words : str
                list of words splitted by spearators like -- ?,! etc.
        """
        words = re.split('\s|(?<!\d)[,.](?!\d)', text)
        return words

    def split_into_sentences(self, text):
        """
        Split the sentences into sentences.

        Parameters
        ----------
        text : str
            list of sentences/ words / paragraph - text data

        Retunrs
        ------
        sentences : str
                list of sentences splitted at "."
        """
        sentences = [each.split('.') for each in self.data]
        return sentences

    def split_into_words(self, text):
        """
        Split the text into words.

        Parameters
        ----------
        text : str
            list of sentences/ words / paragraph - text data

        Retunrs
        ------
        words : str
                list of words splitted at space.
        """
        tokens = [each.split(' ') for each in self.data]
        return tokens
