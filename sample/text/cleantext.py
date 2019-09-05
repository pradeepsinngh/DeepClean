
import numpy as np
import os, copy
import re, string, unicodedata, copy, nltk
import contractions
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

# download
#nltk.download()


def split_by_whitespace(text):
    """
    """
    words = text.split()
    return words

def split_by_words(text):
    """
    """
    words = re.split('\s|(?<!\d)[,.](?!\d)', text)
    return words

def remove_punctuation():
    """
    """
    pass

def convert_to_lowercase(words):
    """
    """
    words = [word.lower() for word in words]
    return words

def split_into_sentences(text):
    """
    """
    sentences = sent_tokenize(text)
    return sentences

def split_into_words(text):
    """
    """
    tokens = word_tokenize(text)
    return tokens

def filter_out_punctuation():
    """
    """
    words = tokens = word_tokenize(text)
    # remove all tokens that are not alphabetic
    words = [word for word in tokens if word.isalpha()]

def filter_out_stopwords(words):
    """
    """
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
