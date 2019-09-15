from deepclean.main import Data
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



class Normalize(Data):
    """
    Normalize is a sub-class  of Data Class which implements various methods
    for normalizing text data.

    ...

    Attributes
    ----------


    """

    def __inti__(self):
        pass

    def remove_non_ascii(self, words):
        """
        Remove non-ASCII characters from list of tokenized words.

        Parameters
        ----------
        words : str
                tokenized words given in list

        Returns
        --------
        new_words : str
                list of words ignoring ASCII

        """
        new_words = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
        return new_words

    def remove_numbers(self, text):
        """
        Remove numbers from given text.

        Parameters
        ----------
        text : str
                data (text) in  words, sentences or paragraph format.

        Returns
        --------
        result : str
                data with numbers removed

        """
        result = re.sub(r'\d+', '', text)
        return result

    def remove_whitespace(self, text):
        """
        Remove white spaces from given data

        Parameters
        ----------
        text : str
                data (text) in  words, sentences or paragraph format.

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        result = text.strip()
        return result


    def clear_blank_lines(self, text, inplace=False):
        """
        Clear blank lines from text data.

        Parameters
        ----------
        text : str
            data (text) in  words, sentences or paragraph format.

        Returns
        ------
        res : str
            text without blank lines

        """
        if not inplace:
            temp = text.copy()

        res =  list(filter(str.strip,[each.rstrip() for each in text]))
        return res


    def to_lowercase(self, text, words = True):
        """
        Convert uppercase characters to lower case throughout the data.

        Parameters
        ----------
        text : str
                data (text) in  words, sentences or paragraph format.

        words : boolean (True/ False)

        Returns
        --------
        new_words : str
                list of new words with all characters converted to lowercase

        """
        new_words = []

        if words == True:
            for word in words:
                new_word = word.lower()
                new_words.append(new_word)
                return new_words
        else:
            return text.lower()

    def remove_punctuation(self, words):
        """
        Remove punctuations from the text/ words/ sentences.

        Parameters
        ----------
        text : str
            data (text) in  words, sentences or paragraph format.

        Returns
        ------
        new_words : list of str
                list of new words with punctuations removed

        """
        new_words = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
        return new_words

    def replace_numbers(self, words):
        """
        Replace numbers (digits - 0,1,2,3) with their words.
        Eg: 0 > One
            1 > Two etc.

        Parameters
        ----------
        words : list of str

        Returns
        ------
        new_words : list of str
                list of words with occurances of numbers converted to words.

        """

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
        """
        Remove stopwords from text.

        Parameters
        ----------
        words : list of str
            list of words

        Returns
        ------
        new_words : new list of words with stop words being removed
        """
        new_words = []
        for word in words:
            if word not in stopwords.words('english'):
                new_words.append(word)
        return new_words

    def stem_words(self, words):
        """
        Applies stemming

        Parameters
        ----------
        words : list of str
            list of words

        Returns
        ------
        stems : new list of words with stemming applied

        """
        stemmer = LancasterStemmer()
        stems = []
        for word in words:
            stem = stemmer.stem(word)
            stems.append(stem)
        return stems

    def lemmatize_verbs(self, words):
        """
        Applies lemmatization

        Parameters
        ----------
        words : list of str
            list of words

        Returns
        ------
        lemmas : new list of words with lemmatization applied

        """
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for word in words:
            lemma = lemmatizer.lemmatize(word, pos='v')
            lemmas.append(lemma)
        return lemmas
