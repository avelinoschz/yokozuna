# https://www.algoexpert.io/questions/binary-search

# Write a function that takes in a sorted array of integers as well as a target integer. 
# The function should use the Binary Search algorithm to determine if the target integer 
# is contained in the array and should return its index if it is, otherwise `-1`.

# If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview 
# section of this question's video explanation before starting to code.

# Sample Input
# array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
# target = 33

# Sample Output
# 3

def binarySearch(array, target):
    low = 0
    high = len(array)-1

    while low <= high:
        mid = (low+high)//2
        if target > array[mid]:
            low = mid+1
        elif target < array[mid]:
            high = mid-1
        else:
            return mid
    return -1
