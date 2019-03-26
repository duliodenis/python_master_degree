#
#  Algorithms: Sorting and Searching: QuickSort
#  Python Techdegree
#
#  Created by Dulio Denis on 3/25/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
import sys
from load import load_numbers
from random import randint

numbers = load_numbers(sys.argv[1])
# ------------------------------------------------
def quicksort(values):
  if len(values) <= 1:
    return values
  less_than_pivot = []
  greater_than_pivot = []
  random_index = randint(0, len(values) - 1)
  pivot = values[random_index]
  del values[random_index]
  for value in values:
    if value <= pivot:
      less_than_pivot.append(value)
    else:
      greater_than_pivot.append(value)
  print("%25s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
  return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

print(numbers)
sorted_numbers = quicksort(numbers)
print(sorted_numbers)