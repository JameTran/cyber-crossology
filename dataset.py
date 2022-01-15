import pandas as pd

def noDups(x):
 return list(dict.fromkeys(x))
#function that removes duplicates from list (values of keys)

df = pd.read_csv("clues.tsv", sep='\t')
#convert tsv file to pandas series (not a dataframe)

df=df.drop(df.columns[[0, 1]], axis=1)
#removes unecessary columns

u = df.select_dtypes(object)
df[u.columns] = u.apply(
    lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))
#function that removes non ascii values from series

dup = df.groupby('answer')['clue'].agg(list)
#combines values for duplicate keys into a list

theDict = dup.to_dict()
#converts pandas series to python dictionary

for i, j in theDict.items():
    theDict[i] = noDups(j)
#removes duplicates from all values 
    
#NO ONE TOUCH THE CODE NO ONE EDIT THE CODE....
#I DONT KNOW WHY IT WORKS BUT IT DOES 