import pandas as pd
import re
from itertools import chain
import nltk
from nltk import regexp_tokenize

def tokenize(raw_data):

    # Read only 'content' column of data
    usecols = ['content']
    df = pd.read_csv(raw_data, usecols = usecols)

    # Create empty list to gather lists of tokens
    # and loop through column to add words
    allWords = []

    for cell in df['content']:
        # words = cell.split()
        # allWords.append(list(words))
        tokens = nltk.word_tokenize(cell)
        tokensREGEX = regexp_tokenize(cell, pattern=r"\s|[.,;']", gaps=True)
        allWords.append(tokens)
    
    # Create flat list from list of lists
    flat_list_raw = [word for inner_list in allWords for word in inner_list]
    flat_list_final = [word for item in flat_list_raw for word in re.split(r'[().,\'"-]', item) if word.strip()]
    # flat_list_final = [word for item in flat_list_raw for word in item.split('.')]
    
    print(len(flat_list_final))
    for i in range(5000,5050):
        print(flat_list_final[i])
           
    return flat_list_final

tokenize('news_sample.csv')

