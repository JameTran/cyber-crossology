from curses.ascii import isalpha, isupper
from hashlib import new


with open('word_list_unclean.txt') as f:
    lines = f.read().splitlines()

def dequote(s):
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

# def first_last_caps(s):
#     a = isupper(s[0])
#     b = isupper(s[-1])
#     if (a == True) and (b == True):
#         return True
#     else:
#         return False
# new_word_list = []
# for i in lines:
#     a = dequote(i)
#     if first_last_caps(a) == False and lines[-1] != i:
#         new_word_list.append(a + "\n")
#     elif first_last_caps(a) == False:
#         new_word_list.append(a)

# fp = open("word_list_clean.txt", 'w')
# fp.writelines(new_word_list)
# fp.close()


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




