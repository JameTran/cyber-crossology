import pandas as pd
import random
import secrets

def convert(string):
    li = list(string.split(","))
    return li

theDict = pd.read_csv(r"theDict.tsv", sep ='\t')
theDict = theDict.drop(theDict.columns[[0]], axis=1)

myDict = theDict.set_index('answer').T.to_dict('list')

def hint(string):
    b = myDict.get(string)[0]
    b = convert(b)
    l = len(b)
    return b[secrets.randbelow(l)]
    
print(hint('POLITICS'))



