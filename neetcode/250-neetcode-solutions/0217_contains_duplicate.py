# 217. Contains Duplicate

# https://neetcode.io/problems/duplicate-integer/question
# https://www.youtube.com/watch?v=3OamzN90kPg

# Easy

# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

from typing import List

# 1. Brute Force
# We can check every pair of different elements in the array and return true if any pair has equal values.
# This is the most intuitive approach because it directly compares all possible pairs, but it is also the least efficient since it examines every combination.

# Time complexity: O(n^2)
# Space complexity: O(1)

# 2. Sorting
# If we sort the array, then any duplicate values will appear next to each other.
# Sorting groups identical elements together, so we can simply check adjacent positions to detect duplicates.
# This reduces the problem to a single linear scan after sorting, making it easy to identify if any value repeats.

# Time complexity: O(n log n) due to the sorting step
# Space complexity: O(1) if we sort in place, otherwise O(n) if we use additional space for sorting. Depends on sorting algorithm.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

# 3. Hash Set

# We can use a hash set to efficiently keep track of the values we have already encountered.
# As we iterate through the array, we check whether the current value is already present in the set.
# If it is, that means we've seen this value before, so a duplicate exists.
# Using a hash set allows constant-time lookups, making this approach much more efficient than comparing every pair.

# Time complexity: O(n)
# Space complexity: O(n)
def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)

    return False


# --------------------------------------------------
# My original description of the problem and solutions based on the video and my own thoughts.

# This problem has a couple of solutions:

# First one is done by just brute force.
# Iterate and compare all the possible combinations.
# This would be: O(n^2) time | O(1) space

# A second way to solve it, is by first sorting the list,
# and then search for adyacent duplicates.
# This would be: O(n log) time | O(1)
# This is not a so bad solution, has a better time complexity
# than first way, and has a good space usage.

# The third way is the one actually implemented, 
# trade off using more space, but getting a much more better
# time complexity. Depending on what we want to prioritize,
# 2nd or 3rd could be valid options.
