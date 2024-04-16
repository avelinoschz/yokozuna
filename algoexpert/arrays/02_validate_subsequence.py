# Validate Subsequence 

# https://www.algoexpert.io/questions/validate-subsequence

# Easy

# Given two non-empty arrays of integers, write a function that determines whether 
# the second array is a subsequence of the first one.

# A subsequence of an array is a set of numbers that aren't necessarily adjacent 
# in the array but that are in the same order as they appear in the array. For instance, 
# the numbers `[1, 3, 4]` form a subsequence of the array `[1, 2, 3, 4]` , and so do the 
# numbers `[2, 4]` . Note that a single number in an array and the array itself are 
# both valid subsequences of the array.

# Sample Input
# array = 15, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]

# Sample Output
# true

# This was the last solution after watching the solution video from AlgoExpert
# O(n) time | O(1) space - where `n` is the length of the input array
def isValidSubsequence_Algo(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

# -----------------------------------------------
# This was my first iteration of the problem, generating a stack
# in reverse order and then pop. Problem here, is space complexity
# Time complexity O(n)
# Space complexity O(n)
def isValidSubsequence1(array, sequence):
    seq_stack = []
    for i in range(len(sequence)-1, -1, -1):
        seq_stack.append(sequence[i])
    
    for n in array:
        if seq_stack and n == seq_stack[-1]:
            seq_stack.pop()

    return len(seq_stack) == 0

# This is another variation of using stack, but traversing the original array
# in reverse order, so there's no need for a second stack, but it will modify
# the original sequence array.
# Time complexity O(n)
# Space complexity O(1)
def isValidSubsequence2(array, sequence):
    for i in range(len(array)-1, -1, -1):
        if not sequence:
            return True
        if array[i] == sequence[-1]:
            sequence.pop()

    return len(sequence) == 0

# This was the second try, now using a two pointer strategy.
# slow pointer is used to traverse in order the sequence array
# Time complexity: O(n)
# Space complexity: O(1)
def isValidSubsequence3(array, sequence):
    slow = 0

    for n in array:
        if slow == len(sequence):
            return True
        if n == sequence[slow]:
            slow += 1

    return slow == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

result = isValidSubsequence_Algo(array, sequence)
print("result:", result)
print("expected:", True)
