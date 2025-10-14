# 26. Remove Duplicates from Sorted Array

# neetcode video solution
# https://www.youtube.com/watch?v=DEJAZBq0FDA

# Time complexity: O(n)
# Space complexity: O(1)

def removeDuplicates(nums):
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