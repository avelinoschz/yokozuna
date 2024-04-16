# 1929. Concatenation of Array

# https://leetcode.com/problems/concatenation-of-array/description/

# Easy

# Given an integer array nums of length n, you want to create an array 
# ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] 
# for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

nums = [2,3,4,5,6]
ans = [0] * len(nums) * 2

print(nums)
print(ans)
print(len(ans))

nums_idx = 0
for i in range(len(ans)):
    if nums_idx >= len(nums):
        nums_idx = 0
    ans[i] = nums[nums_idx]
    nums_idx += 1
    
print(ans)

# easy python way
# ans = nums * 2