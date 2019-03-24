#
#  Data Structures: Merge Sort: Ensuring Correctness
#  Python Techdegree
#
#  Created by Dulio Denis on 3/24/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
def merge_sort(list):
    '''
    Sorts a list in ascending order.
    Returns a new sorted list.

    Divide:  Find the midpoint of the list and divide into sublists.
    Conquer: Recursively sort the sublists created in previous step.
    Combine: Merge the sorted sublists created in the previous step.

    Takes O(kn log n) quasilinear time overall.
    An optimization would be to refactor the splices in the split.
    '''
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    '''
    Divide the unsorted list at midpoint into sublists.
    Returns two sublists - left and right.
    Takes O(k log n) logarithmic time due to the k splices.
    '''
    midpoint = len(list) // 2
    left = list[:midpoint]
    right = list[midpoint:]
    
    return left, right

def merge(left, right):
    '''
    Merges two lists (arrays), sorting them in the process.
    Returns a new merged list.
    Takes an O(n) number of merge steps.
    '''
    merged_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    
    while i < len(left):
        merged_list.append(left[i])
        i += 1

    while j < len(right):
        merged_list.append(right[j])
        j += 1
    
    return merged_list

def verify_sorted(list):
    '''
    Recursively verifies if the passed list is sorted.
    '''
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list [1] and verify_sorted(list[1:]) 

my_list = [54, 62, 4, 121]
print(merge_sort(my_list))

my_second_list = [54, 62, 1, 1001, 4, 8, 20, 5, 121]
print(merge_sort(my_second_list))

print(verify_sorted(my_list))
print(verify_sorted(merge_sort(my_list)))
