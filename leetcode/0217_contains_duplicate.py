# 217. Contains Duplicate

# https://leetcode.com/problems/contains-duplicate/description/

# Easy

# Given an integer array nums, return true if any value appears at 
# least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Time complexity: O(n)
# Space complexity: O(n)
from typing import List

def containsDuplicate(self, nums: List[int]) -> bool:
    count = set()
    for n in nums:
        if n in count:
            return True
        count.add(n)
    
    return False
