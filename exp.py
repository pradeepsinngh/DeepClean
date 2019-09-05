#import cleantext as ct
#import sample.cleantext as ct
import sample.text.cleantext as sp
#from sample.cleantext import split_by_words, split_by_whitespace

filename = 'data.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

res = sp.split_by_whitespace(text)
print(res)

res2 = sp.split_by_words(text)
print(res2)
