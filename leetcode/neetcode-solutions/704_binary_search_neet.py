# neetcode video solution
# https://www.youtube.com/watch?v=s4DPM8ct1pI

# Time complexity: O(log n)
# Space complexity: O(1)

from typing import List

def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) -1 

    while l <= r:
        # in strong typed langauges, there is a possible error caused by
        # integer overflow. There could be a case where de `nums` array
        # is so large, that the sum of left + right surpasses the max value
        # of an integer. This is a way to calculate the mid point
        # m = l + ((r - l) // 2)
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    
    return -1


nums = [-1, 2, 5, 7, 9]
target = 5

result = search(nums, target)
print(result)