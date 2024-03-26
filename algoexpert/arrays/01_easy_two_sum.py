# Two Number Sum

# https://www.algoexpert.io/questions/two-number-sum

# Write a function that takes in a non-empty array of distinct integers and an 
# integer representing a target sum. If any two numbers in the input array sum 
# up to the target sum, the function should return them in an array, in any order. 
# If no two numbers sum up to the target sum, the function should return an empty array.

# Note that the target sum has to be obtained by summing two different integers 
# in the array; you can't add a single integer to itself in order to obtain the 
# target sum.

# You can assume that there will be at most one pair of numbers summing up to 
# the target sum.

# Sample Input
# array = 13, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10

# Sample Output
# [-1, 11] // the numbers could be in reverse order

# There are none AlgoExpert solutions, since those were basically same as mine.

# -----------------------------------------------

# This was my first try, using map (dictionary in python)
# Time complexity: O(n)
# Space complexity: O(n)
def twoNumberSum1(array, targetSum):
    nums_seen = {}
    for n in array:
        com = targetSum - n
        if com in nums_seen:
            return [n, com]
        nums_seen[n] = True

    return []

# Since I didn't need key-value pair, this is a second try
# using only a set. Same functionality and space.
# Time complexity: O(n)
# Space complexity: O(n)
def twoNumberSum2(array, targetSum):
    nums_seen = set()
    for n in array:
        com = targetSum - n
        if com in nums_seen:
            return [n, com]
        nums_seen.add(n)

    return []

# This is the implementation of using two pointers, after sorting
# I still need to review sorting at this point, so will use
# Python's built in sorting algorithm, which underlying uses Tim Sort

# Time complexity: O(n log (n))
# Space complexity: O(1)
def twoNumberSum3(array, targetSum):
    array.sort() # Tim sort time complexity is O(n log (n))

    # This while loop is O(n) which sums to the O(n log (n))
    # ending up being O(n log (n))
    l, r = 0, len(array)-1
    while l < r:
        if array[l] + array[r] > targetSum:
            r -= 1
        elif array[l] + array[r] < targetSum:
            l =+ 1
        elif array[l] + array[r] == targetSum:
            return [array[l], array[r]]
    return []
            
array = [3, 5, -1, 8, 11, 1, -1, 6]
targetSum = 10
expected = [-1, 11]

result = twoNumberSum3(array, targetSum)
print("result:", result)
print("expected:", expected)

