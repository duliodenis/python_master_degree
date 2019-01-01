#
#  word_count
#  Python Techdegree
#
#  Created by Dulio Denis on 12/9/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Make a function named word_count which accepts a single argument which will be a string. 
#  The function needs to return a dictionary. 
#  The keys in the dictionary will be each of the words in the string, lowercased. 
#  The values will be how many times that particular word appears in the string.
# ------------------------------------------------
# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.
def word_count(input_string):
    # take the input string and lowercase it
    lowered_input_string = input_string.lower()
    # seperate the sting into a word list
    words = lowered_input_string.split()

    # the return response is a dictionary of word keys
    return_dict = {}

    # go through each word and add them to the return response dictionary
    for word in words:
        if word in return_dict:
            return_dict[word] += 1
        else:
            return_dict[word] = 1
    return return_dict

print(word_count("I do not like it Sam I Am"))