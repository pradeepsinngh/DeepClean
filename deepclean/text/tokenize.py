import re
from bs4 import BeautifulSoup
from deepclean.text.main import CleanText

class Tokenize(CleanText):
    """
    A class used to represent Tokenization techniques for text.

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    split_by_words(text)
        Return the sentences splitted by white spaces.

    split_by_words(text)
        Retunr

    split_into_sentences(text)

    split_into_words(text)
    """

    def __inti__(self):
        pass

    def split_by_whitespace(self, text):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        text : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        words = text.split()
        return words

    def split_by_words(self, text):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        text : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        words = re.split('\s|(?<!\d)[,.](?!\d)', text)
        return words

    def split_into_sentences(self, text):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        text : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        sentences = [each.split('.') for each in self.data]
        return sentences

    def split_into_words(self, text):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        text : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        tokens = [each.split(' ') for each in self.data]
        return tokens
