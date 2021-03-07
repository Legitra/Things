'''
TODO:

> optimise the 'S[index] in const/vowels' into a function to reduce duplicated code
> optimise minion_games() to reduce duplicated code
> fails tests 4, 5, 6, 8, 10, 12, 13, 14
--> uses too much resources --> test times out
'''
from collections import Counter
alphabet = [(chr(ord('A')+i)) for i in range(26)]       #list of alphabet in capitals
vowels   = ['A','E','I','O','U']                        #list of vowels
const    = [a for a in alphabet if a not in vowels]     #list of constants made from [alphabet] and [vowels]

def get_words(S,v):
    '''
    Takes two inputs, a string and a bool; and returns a list.
    string, 'S' is the word players are given.
    bool 'v' is True if the player has to start with vowels.
    returned list is the "words" found by each character.
    '''
    words = []
    if v == False:                                      #player 1 uses constants
        for index in range (0,len(S)):                  #for each character in the given string
            if S[index] in const:                       #if the character is a constant
                
                max_len = 0
                temp_word = ""
                while (max_len + index) < (len(S)):     #while [counter] + [index] is less than
                                                        #              the length of the given string
                    temp_word += S[index + max_len]     #create a new word starting at [index],
                                                        #             + next letter [counter] in word
                    words.append(temp_word)             #add this new word to the list of found words
                    max_len += 1                        #increment counter
        
    else:                                               #player 2 uses vowels
        for index in range (0,len(S)):                  #for each character in the given string
            if S[index] in vowels:                      #if the character is a vowel
                
                max_len = 0
                temp_word = ""
                while (max_len + index) < (len(S)):     #while [counter] + [index] is less than
                                                        #              the length of the given string
                    temp_word += S[index + max_len]     #create a new word starting at [index],
                                                        #             + next letter [counter] in word
                    words.append(temp_word)             #add this new word to the list of found words
                    max_len += 1                        #increment counter

    return words

def minions_game(S):
    '''
    Takes one input, a string, 'S' and prints the winner of the game.
    string, 'S' is the word players are given.
    '''
    player_1 = 0
    player_2 = 0

    for w in Counter(get_words(S,False)).values():
        player_1 += w
    for w in Counter(get_words(S,True)).values():
        player_2 += w
    
    if player_1 > player_2:
        print("Stuart "+ str(player_1))
    elif player_1 < player_2:
        print("Kevin " + str(player_2))
    else:
        print("Draw")
        
    return
