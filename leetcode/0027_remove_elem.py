# 27. Remove Element

# https://leetcode.com/problems/remove-element/description/

# Easy

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.

# Return k.

# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Time complexity: O(n)
# Space complexity: O(1)
def removeElement(nums, val):
    l = 0
    for r in range(0, len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1

    return l
        
nums = [0,1,2,2,3,0,4,2]
val = 2

expected_nums = [0,1,3,0,4]
expected_k = 5

k = removeElement(nums, val)
print("output nums:", nums)
print("output k:", k)
print("truncated", nums[:k])

# the problem states that the first k numbers
# need to be unique
print(expected_nums == nums[:k])
print(expected_k == k)

# --------------------------------------------------
# Solution: March 11, 2024
# def removeElement(self, nums, val):
#     if not nums:
#         return 0

#     write_index = 0
#     for i in range(0, len(nums)):
#         if nums[i] != val:
#             if write_index != i:
#                 nums[write_index] = nums[i]
#             write_index += 1
#     return write_index