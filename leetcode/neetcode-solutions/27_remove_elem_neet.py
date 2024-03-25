# 27. Remove Element

# neetcode video solution
# https://www.youtube.com/watch?v=Pcd1ii9P9ZI

# Time complexity: O(n)
# Space complexity: O(1)

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
        
# nums = [3,2,2,3] 
# val = 3
# expected_nums = [2,2]
# expected_k = 2

nums = [0,1,2,2,3,0,4,2]
val = 2
expected_nums = [0,1,3,0,4]
expected_k = 5

print("original nums: ", nums)
k = removeElement(nums, val)
print("val to remove:", val)
print("output nums:", nums)
print("truncated", nums[:k])
print("output k:", k)
print("pass nums: ", expected_nums ==  nums[:k])
print("pass k: ", expected_k == k)
