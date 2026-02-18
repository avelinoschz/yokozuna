
# https://algomap.io/problems/find-closest-number-to-zero
# https://www.youtube.com/watch?v=dLlKA5DQKYs&t=199s

# Detailed Explanation

# Understanding the Problem: Find Closest Number to Zero

# The Find Closest Number to Zero problem is a classic array algorithm challenge frequently encountered in technical interviews and coding practice platforms like LeetCode. The objective is to identify the integer in a list that is numerically closest to zero. If there is a tie — for instance, both -2 and 2 — the positive number should be returned.

# Problem Statement

# Given an array of integers, return the number closest to zero. If there are two equally close values (one negative and one positive), return the positive one. For example, given the input [-4, -2, 1, 4, 2], both -2 and 2 are at the same distance from zero, but the correct answer is 2.

# Algorithmic Approach

# This problem is typically solved using a linear scan algorithm. We initialize a variable, commonly called closest, with the first value of the array. As we iterate through the array, we compare each element using absolute value comparison:

# If the absolute value of the current number is less than that of closest, update closest.
# If the absolute values are the same, choose the positive number.
# This logic ensures that we return the number closest to zero and correctly handle tie-breakers in favor of positive values.

# Time and Space Complexity

# The solution operates in O(n) time complexity, making a single pass through the array of length n. It uses O(1) space complexity since no additional data structures are required beyond a few variables.

# Edge Cases

# This problem requires careful attention to detail. Common edge cases include:

# An array containing only one element
# Presence of both x and -x
# All elements being negative or all being positive
# Correct handling of these edge cases ensures robustness and correctness of the algorithm.

# Use Cases and Relevance

# This type of problem teaches key programming concepts such as comparison operations, absolute value logic, and array traversal. It is commonly used to assess fundamental algorithmic thinking in entry-level coding interviews and is relevant in real-world scenarios such as:

# Sensor data normalization
# Financial deviation analysis
# Error minimization logic
# Summary

# The Find Closest Number to Zero in an Array problem is simple but conceptually rich. It reinforces the importance of precise control structures and teaches developers how to implement custom tie-breaking rules using clean logic. Due to its clarity and relevance, it remains a staple among introductory-level data structure and algorithm problems.

# Time: O(n)
# Space: O(1)
from typing import List
 
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest