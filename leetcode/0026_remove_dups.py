# 26. Remove Duplicates from Sorted Array

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Easy

# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element 
# appears only once. The relative order of the elements should 
# be kept the same. Then return the number of unique elements 
# in nums.

# Consider the number of unique elements of nums to be k, to 
# get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums 
# contain the unique elements in the order they were present 
# in nums initially. The remaining elements of nums are not 
# important as well as the size of nums.
# Return k.
def removeDuplicates(nums):
        if not nums:
            return 0

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1

        return l

nums = [0,0,1,1,1,2,2,3,3,4]
expected_nums = [0,1,2,3,4]
expected_k = 5

k = removeDuplicates(nums)
print("output nums:", nums)
print("output k:", k)
print("truncated", nums[:k])

# the problem states that the first k numbers
# need to be unique
print(expected_nums == nums[:k])
print(expected_k == k)
