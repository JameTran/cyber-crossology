import pandas as pd

def convert(string):
    li = list(string.split(","))
    return li

theDict = pd.read_csv(r"theDict.tsv", sep ='\t')
theDict = theDict.drop(theDict.columns[[0]], axis=1)

myDict = theDict.set_index('answer').T.to_dict('list')
b = myDict.get('GOD')[0]
b = convert(b)

print(b)



