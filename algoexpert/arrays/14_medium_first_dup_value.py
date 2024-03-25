# First Duplicate Value

# https://www.algoexpert.io/questions/first-duplicate-value

# Given an array of integers between `1` and `n`, inclusive, where `n` is the length 
# of the array, write a function that returns the first integer that appears more than 
# once (when the array is read from left to right).

# In other words, out of all the integers that might occur more than once in the input 
# array, your function should return the one whose first duplicate value has the minimum 
# index.

# If no integer appears more than once, your function should return `-1`.

# Note: that you're allowed to mutate the input array.

# Sample Input #1
# array = 12, 1, 5, 2, 3, 3, 4]

# Sample Output #1
# 2 // 2 is the first integer that appears more than once.
# // 3 also appears more than once, but the second 3 appears after the second 2.

# Sample Input #2
# array = [2, 1, 5, 3, 3, 2, 4]

# Sample Output #2
# 3// 3 is the first integer that appears more than once.
# // 2 also appears more than once, but the second 2 appears after the second 3.

# -----------------------------------------------

# First, I though this was only a re-write of the leetcode problem 217. Contains Duplicate
# After reading the description, understand it wasn't. Could be solved in the same way
# But it has different constraints, that make it possible to solve in other way.

# O(n) time | O(n) space
def firstDuplicateValue(array):
    hashset = set()

    for n in array:
        if n in hashset:
            return n
        hashset.add(n)
    
    return -1

# For this case, it was important to read at the details.
# Description mentioned that the integers inside the array, were from 1 to n
# being n the length of the array. Meaning that all the array integers, could
# be used as indexes. Another hint was around that we could modify the array.
# With these two hints, we could achieve this second implementation.

# O(n) time | O(1) space
def firstDuplicateValue2(array):
    for n in array:
        a = abs(n)
        if array[a-1] < 0:
            return a
        array[a-1] *= -1
    
    return -1
