# Quiz: Intro to Algorithms: Algorithms in Code (3 Questions)
## Python Techdegree
## Created by Dulio Denis on 3/23/19.

### Quiz Question 1 of 3
Inspecting the code for the linear search algorithm (which I've included below for convenience), there is no single step that has a time complexity greater than O(1). Why then do we say that the algorithm has a linear runtime?
``` def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
```
> In the worst case the algorithm has to compare every item in the list

### Quiz Question 2 of 3
Given the following functions, which of the two is a recursive function?
```def sum(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    return sum
```

```def sum_values(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum_values(list[1:])
```

> sum_values()

### Quiz Question 3 of 3
What is the precondition for the binary search algorithm?
> The data must be sorted
