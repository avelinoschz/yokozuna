# Sorted Squared Array

# https://www.algoexpert.io/questions/sorted-squared-array

# Easy

# Write a function that takes in a non-empty array of integers that are 
# sorted in ascending order and returns a new array of the same length 
# with the squares of the original integers also sorted in ascending order.

# Sample Input
# array = 11, 2, 3, 5, 6, 8, 9]

# Sample Output
# [1, 4, 9, 25, 36, 64, 81]

# These are the solutions from AlogExpert

# This first one relies on calculate the squares and then sort the result array.
# O(n log n) time | O(n) space - where `n` is the length of the input array
def sortedSquaredArray_Algo1(array):
    sortedSquares = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value

    sortedSquares.sort()
    return sortedSquares

# This second solution uses a two pointer (or three) technique. 
# First create an array full of zeroes, and while traversing 
# at the start and end of the array, add to the end of the
# output array the one that's bigger.

# O(n) time | O(n) space - where `n` is the length of the input array
def sortedSquaredArray_Algo2(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largestValueIdx = len(array)-1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largestValue = array[largestValueIdx]

        if abs(smallerValue) > abs(largestValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largestValue * largestValue
            largestValueIdx -= 1

    return sortedSquares 

# -----------------------------------------------
# My solution for the problem.
# Time complexity: O(n)
# Space complexity: O(n)
def sortedSquaredArray(array):
    start = 0
    end = len(array)-1
    output = [0] * len(array)

    for i in range(len(array)-1, -1, -1):
        square_start = array[start] * array[start]
        square_end = array[end] * array[end]
        if square_start > square_end:
            output[i] = square_start
            start += 1
        else:
            output[i] = square_end
            end -= 1
    
    return output
    