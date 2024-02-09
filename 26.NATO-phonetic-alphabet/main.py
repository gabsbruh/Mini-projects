import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv') # read from csv as pd.df
df_dict = {row[0]: row[1] for (index, row) in df.iterrows()} # change format from pd.df to a dict
print([df_dict[key.upper()] for key in input('Write a word to spell:')]) # print list of words literating from user's input
