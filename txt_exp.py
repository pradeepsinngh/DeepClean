
import deepclean.text.main as dc_text
import deepclean.text.tokenize as tk
import deepclean.text.denoise as dn
import deepclean.text.normalize as nz


filename = 'data.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

ob = dc_text.CleanText(filename)

wrds = ob.getSummary(text)
print(wrds)
