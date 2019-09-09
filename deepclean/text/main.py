
import os, copy

class CleanText(object):

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
        return [word for sent in lis for word in sent]

    # create copy of your data
    def copy(self):
        temp = copy.deepcopy(self)
        return temp

    # checks whether it has file path as argument
    def _file_or_not(self,arg):
        if os.path.isfile(arg):
            return True
        else:
            return False,"only supports .txt for now"

    # this reader is flexible enough to process file or will return the data
    # if list is being passed to the function.
    def _reader(self,file):
        if type(file)==str and self._file_or_not(file)==True:
            with open(file,'r') as f:
                return f.readlines(),file

        elif type(file)==str:
            return file.split('\n'),''

        else: return file,''


    # removes all the blank line from the text file
    # returns list
    def clear_blank_lines(self,inplace=False):
        """
        Clear blank lines
        """
        if not inplace: self = self.copy()
        self.data =  list(filter(str.strip,[each.rstrip() for each in self.data]))
        return self

    def getSummary(self, text):
        print('Filename:', self.file_name)
        print('Number of Words:', self.count_words)
        print('Number of Sentences:', self.count_sentences)
