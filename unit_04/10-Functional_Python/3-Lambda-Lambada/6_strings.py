#
#  Functional Python: The Lambda Lambada (Lambdas)
#  Python Techdegree
#
#  Created by Dulio Denis on 3/22/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Lambda Challenge Two
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Use reduce() and a lambda to find the longest
#  string in strings.
#  Save this value in the variable longest.
#  Remember, reduce() takes two arguments and you
#  can write an if statement like:
#  give_me_this if this_thing > that_thing else give_me_that.
from functools import reduce

strings = [
    "Do not take life too seriously. You will never get out of it alive.",
    "My fake plants died because I did not pretend to water them.",
    "A day without sunshine is like, you know, night.",
    "Get your facts first, then you can distort them as you please.",
    "My grandmother started walking five miles a day when she was sixty. She's ninety-seven now and we don't know where she is.",
    "Life is hard. After all, it kills you.",
    "All my life, I always wanted to be somebody. Now I see that I should have been more specific.",
    "Everyone's like, 'overnight sensation.' It's not overnight. It's years of hard work.",
]

longest = reduce(lambda string1, string2: string1 if len(string1) > len(string2) else string2, strings)
print(longest)
