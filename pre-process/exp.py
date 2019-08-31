import cleantext as ct
import textcleaner as tc

filename = 'data.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

res = ct.split_by_whitespace(text)
print(res)

res2 = ct.split_by_words(text)
print(res2)
