import numpy as np
import os, copy
import re, string, unicodedata, copy, nltk
import contractions
import inflect
from bs4 import BeautifulSoup


def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
return text

def replace_contractions(text):
    """Replace contractions in string of text"""
    return contractions.fix(text)
