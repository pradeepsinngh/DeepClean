
import os, copy

class CleanText(object):

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

    filename = ''
    text = []
    nsentences = 0
    nwords = 0
    each_word_count = {}
    tokens = []
    words = []
    sentences = []

    def __init__(self,fname=''):

        if fname:
            self.data, file =  self._reader(fname)
            self.words = [each.split(' ') for each in self.data]
            self.count_words = len([word for sent in self.words for word in sent])
            self.count_sentences = sum(each.count('.') for each in self.data)
            temp = self._flatlist(self.words)
            self.each_word_count = {x:temp.count(x) for x in temp}
            self.file_name = file.split('\\')[-1]
        else:
            pass

    def _flatlist(self,lis):
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
        return [word for sent in lis for word in sent]

    # create copy of your data
    def copy(self):
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
        temp = copy.deepcopy(self)
        return temp

    # checks whether it has file path as argument
    def _file_or_not(self,arg):
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
        if os.path.isfile(arg):
            return True
        else:
            return False,"only supports .txt for now"

    # this reader is flexible enough to process file or will return the data
    # if list is being passed to the function.
    def _reader(self,file):
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
        if type(file)==str and self._file_or_not(file)==True:
            with open(file,'r') as f:
                return f.readlines(),file

        elif type(file)==str:
            return file.split('\n'),''

        else: return file,''


    # removes all the blank line from the text file
    # returns list
    def clear_blank_lines(self,inplace=False):
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
        if not inplace: self = self.copy()
        self.data =  list(filter(str.strip,[each.rstrip() for each in self.data]))
        return self

    def getSummary(self, text):
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
        print('Filename:', self.file_name)
        print('Number of Words:', self.count_words)
        print('Number of Sentences:', self.count_sentences)
