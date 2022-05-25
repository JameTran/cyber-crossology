from curses.ascii import isalpha, isupper
from hashlib import new
import nltk
#nltk.download('words')
from nltk.corpus import words


with open('word_list_unclean.txt') as f:
    lines = f.read().splitlines()

def dequote(s):
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s


##clean thewords.txt
with open('thewords.txt') as ff:
    l = ff.read().splitlines()

count = 0
the_words_alpha = []
for i in l:
    # if count == 50:
    #     break
    if i.isalpha() == True:
        the_words_alpha.append(i.upper())
        count += 1


words_upper = []
for w in words.words():
    words_upper.append(w.upper())

new_list = []
for i in the_words_alpha:
    print("uwu \n")
    if i in words_upper:
        if i == the_words_alpha[-1]:
            new_list.append(i)
            print(i)
        else:
            new_list.append(i + "\n")
            print(i + "\n")

fpp = open("the_words_singular.txt", 'w')
fpp.writelines(new_list)
fpp.close()


        






