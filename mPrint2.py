# Deal with the format of Greek Letters
import pandas as pd
rfile = open('greek_letter.txt')
mfile = pd.read_csv('greek_letter.txt')
mfile.to_csv('greek_letter2.csv')
print('Suc')