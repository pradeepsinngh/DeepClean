from deepclean.text.main import CleanText
import re, string, unicodedata
import contractions
import inflect
from bs4 import BeautifulSoup

import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('stopwords')
nltk.download('wordnet')



class Normalize(CleanText):
    """
    Text normalization is the process of transforming text into a single canonical form that it might not have had before.
    """

    def __inti__(self):
        pass

    def remove_non_ascii(self, words):
        """Remove non-ASCII characters from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
        return new_words

    def remove_numbers(self, text):
        """Remove numbers from given text."""
        result = re.sub(r'\d+', '', text)
        return result

    def remove_whitespace(self, text):
        """ Remove white spaces"""
        result = text.strip()
        return result


    def to_lowercase(self, text, words = True):
        """Convert all characters to lowercase from text or list of tokenized words"""
        new_words = []

        if words == True:
            for word in words:
                new_word = word.lower()
                new_words.append(new_word)
                return new_words
        else:
            return text.lower()

    def remove_punctuation(self, words):
        """Remove punctuation from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
        return new_words

    def replace_numbers(self, words):
        """Replace all interger occurrences in list of tokenized words with textual representation"""
        p = inflect.engine()
        new_words = []
        for word in words:
            if word.isdigit():
                new_word = p.number_to_words(word)
                new_words.append(new_word)
            else:
                new_words.append(word)
        return new_words

    def remove_stopwords(self, words):
        """Remove stop words from list of tokenized words"""
        new_words = []
        for word in words:
            if word not in stopwords.words('english'):
                new_words.append(word)
        return new_words

    def stem_words(self, words):
        """Stem words in list of tokenized words"""
        stemmer = LancasterStemmer()
        stems = []
        for word in words:
            stem = stemmer.stem(word)
            stems.append(stem)
        return stems

    def lemmatize_verbs(self, words):
        """Lemmatize verbs in list of tokenized words"""
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for word in words:
            lemma = lemmatizer.lemmatize(word, pos='v')
            lemmas.append(lemma)
        return lemmas
