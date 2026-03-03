# 1. Two Sum

# https://neetcode.io/problems/two-integer-sum/question
# https://www.youtube.com/watch?v=KLlXCFG5TnA

# Easy 

# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:
# Input: nums = [3,4,5,6], target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:
# Input: nums = [4,5,6], target = 10
# Output: [0,2]

# Example 3:
# Input: nums = [5,5], target = 10
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000
# Only one valid answer exists.

# 1. Brute Force
# We can check every pair of different elements in the array and return the first pair that sums up to the target. This is the most intuitive approach but it's not the most efficient.

# Time complexity: O(n^2)
# Space complexity: O(1)

# 2. Sorting
# We can sort the array and use two pointers to find the two numbers that sum up to the target. This is more efficient than the brute force approach. This approach is similar to the one used in Two Sum II (https://neetcode.io/problems/two-integer-sum-ii).

# Time complexity: O(nlogn)
# Space complexity: O(n)
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []
    
# 3. Hash Map (Two Pass)
# We can use a hash map to store the value and index of each element in the array. Then, we can iterate through the array and check if the complement of the current element exists in the hash map. The complement must be at a different index, because we can't use the same element twice.
# By using a hashmap, we can achieve a time complexity of O(n) because the insertion and lookup time of a hashmap is O(1).

# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []
    
# 4. Hash Map (One Pass)
# We can solve the problem in a single pass by iterating through the array and checking if the complement of the current element exists in the hash map.
# If it does, we return the indices of the current element and its complement. If not, we store the current element in the hash map. This guarantees that we will never use the same element twice, but we still check every element in the array.

# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
