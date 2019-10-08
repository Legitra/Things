#check if palidrome
from math import ceil

def pali_check(word):
    for i in range(len(word)):
        if i == ceil((len(word) / 2 )):
            break
        if word[i] == word[-(i+1)]:
            pass
        else:
            return False
    return True

checking = input('Input a word: ').upper()

if pali_check(checking) == False:
    print('{0} is not a palidrome'.format(checking))
elif pali_check(checking) == True:
    print('{0} is a palidrome'.format(checking))
