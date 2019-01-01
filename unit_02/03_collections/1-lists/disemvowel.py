#
#  disemvowel
#  Python Techdegree
#
#  Created by Dulio Denis on 12/6/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  disemvowel takes a single word as a parameter and then returns that word at the end.
#  Inside of the function, all of the vowels ("a", "e", "i", "o", and "u") are removed from the word. 
#  NOTE: be sure to look for both uppercase and lowercase vowels!

def disemvowel(word_as_string):
    print("Start > " + word_as_string)
    word = list(word_as_string)

    vowels = ["a", "e", "i", "o", "u"]

    keep_list = []

    for letter in word:
        if letter.lower() not in vowels:
            keep_list.append(letter)
    
    return ''.join(keep_list)

print('Starting program')
new_string = disemvowel("hello there. Alaska is AWESOME!")
print("End   > " + new_string)
