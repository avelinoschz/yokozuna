# 26. Remove Duplicates from Sorted Array

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

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
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        write_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if write_index != i:
                    nums[write_index] = nums[i]
                write_index += 1
        return write_index

# nums = [1,2]
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
