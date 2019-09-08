import re, string
import contractions
#import inflect
from bs4 import BeautifulSoup
from deepclean.text.main import CleanText


class Denoise(CleanText):

    def __init__(self):
        pass

    def strip_html(self, text):
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text()

    def remove_between_square_brackets(self, text):
        return re.sub('\[[^]]*\]', '', text)

    def denoise_text(self, text):
        text = strip_html(text)
        text = remove_between_square_brackets(text)
        return text

    def replace_contractions(self, text):
        """Replace contractions in string of text"""
        return contractions.fix(text)
