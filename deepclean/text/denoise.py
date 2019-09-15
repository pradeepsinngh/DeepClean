import re, string
import contractions
from bs4 import BeautifulSoup
from deepclean.main import Data


class Denoise(Data):
    """
    Denoise is a sub-class  of Data Class which implements various methods
    for denoising text data.

    ...

    Attributes
    ----------


    """

    def __init__(self):
        pass

    def strip_html(self, text):
        """
        Remove html tags from data.

        Parameters
        ----------
        text : str
            sentences/ words / paragraph - text data

        Returns
        ----------
        no_html_data : str
                data with html tags removed

        """
        soup = BeautifulSoup(text, "html.parser")
        no_html_data = soup.get_text()
        return no_html_data

    def remove_between_square_brackets(self, text):
        """
        Remove special characters from given text.

        Parameters
        ----------
        text : str
            list of sentences/ words / paragraph - text data

        Returns
        ------
        new_text : str
                new data with special characters removed
        """

        new_text = re.sub('\[[^]]*\]', '', text)
        return new_text


    def replace_contractions(self, text):
        """
        Replaces contractions from data.

        Parameters
        ----------
        text : str
            list of sentences/ words / paragraph - text data

        Returns
        ------
        new_text : str
                new data with contractions removed
        """

        rep_contractions = contractions.fix(text)
        return rep_contractions
