# 26. Remove Duplicates from Sorted Array

# Question: https://neetcode.io/problems/remove-duplicates-from-sorted-array/question
# Neetcode video solution: https://www.youtube.com/watch?v=DEJAZBq0FDA

# Two Pointers

# Easy

# Time complexity: O(n)
# Space complexity: O(1)

# You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.

# After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

# Note:

# The order of the unique elements should remain the same as in the original array.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain all the unique elements.
# Return k as the final result.

# Example 1:

# Input: nums = [1,1,2,3,4]

# Output: [1,2,3,4]
# Explanation: You should return k = 4 as we have four unique elements.

# Example 2:

# Input: nums = [2,10,10,30,30,30]

# Output: [2,10,30]
# Explanation: You should return k = 3 as we have three unique elements.

# Constraints:

# 1 <= nums.length <= 30,000
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

# 1. Sorted Array
# A set automatically removes duplicates, and a sorted set maintains order. We insert all elements into a sorted set, then copy the unique elements back to the original array. 
# This approach is simple but uses extra space and doesn't take advantage of the array already being sorted.

# For Leetcode, this is not a valid solution, because it uses extra space and doesn't modify the input array in-place as required by the problem statement.

# Time complexity: O(n log n)
# Space complexity: O(n)
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)


# 2. Two Pointers - I
# Since the array is sorted, duplicates are adjacent. We use two pointers: one (l) marks where to place the next unique element, and another (r) scans through the array. 
# When r finds a new value (different from what's at l), we copy it to position l and advance both pointers. This modifies the array in-place.

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        l = r = 0
        while r < n:
            nums[l] = nums[r]
            while r < n and nums[r] == nums[l]:
                r += 1
            l += 1
        return l


# 3. Two Pointers - II
# A more elegant approach: we compare each element with its predecessor. Since duplicates are consecutive in a sorted array, an element is unique if it differs from the one before it. 
# We maintain a write pointer that only advances when we find a new unique value.

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l