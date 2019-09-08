import re
from bs4 import BeautifulSoup
from deepclean.text.main import CleanText


class Tokenize(CleanText):

    def __inti__(self):
        pass


    def split_by_whitespace(self, text):
        """
        """
        words = text.split()
        return words

    def split_by_words(self, text):
        """
        """
        words = re.split('\s|(?<!\d)[,.](?!\d)', text)
        return words

    def split_into_sentences(self, text):
        """
        """
        sentences = [each.split('.') for each in self.data]
        return sentences

    def split_into_words(self, text):
        """
        """
        tokens = [each.split(' ') for each in self.data]
        return tokens
