#
#  Algorithms: Sorting and Searching: Bogus Sort
#  Python Techdegree
#
#  Created by Dulio Denis on 3/25/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])
# ------------------------------------------------
def is_sorted(values):
  for index in range(len(values) - 1):
    if values[index] > values[index + 1]:
      return False
  return True

def bogo_sort(values):
  attempts = 0
  while not is_sorted(values):
    print(attempts)
    random.shuffle(values)
    attempts += 1
  return values

print(bogo_sort(numbers))
