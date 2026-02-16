# 1929. Concatenation of Array

# https://leetcode.com/problems/concatenation-of-array/description/

# Difficulty: Easy

# Given an integer array nums of length n, you want to create an array 
# ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] 
# for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

# Example 1:
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

# Example 2:
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]

# Constraints:
# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000

# Time complexity: O(n)
# Space complexity: O(n)
def getConcatenation(nums):
        ans = nums.copy()
        for i in range(len(nums)):
            ans.append(nums[i])

        return ans

nums = [2,3,4,5,6]
print(getConcatenation(nums))

def getConcatenation2(nums):
    n = len(nums)
    for i in range(n):
        nums.append(nums[i])
    return nums

nums2 = [2,3,4,5,6]
print(getConcatenation2(nums2))

# --------------------------------------------------
# Super pythonic way
# ans = nums * 2

# --------------------------------------------------
# Solution: March 11, 2024
# def getConcatenation(nums):
#     ans = [0] * len(nums) * 2

#     nums_idx = 0
#     for i in range(0, len(ans)):
#         if nums_idx >= len(nums):
#             nums_idx = 0
#         ans[i] = nums[nums_idx]
#         nums_idx += 1
#     return ans