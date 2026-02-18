# 2239. Find Closest Number to Zero

# https://leetcode.com/problems/find-closest-number-to-zero/description/

# Difficulty: Easy

# Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
# If there are multiple answers, return the number with the largest value.

# Example 1:

# Input: nums = [-4,-2,1,4,8]
# Output: 1
# Explanation:
# The distance from -4 to 0 is |-4| = 4.
# The distance from -2 to 0 is |-2| = 2.
# The distance from 1 to 0 is |1| = 1.
# The distance from 4 to 0 is |4| = 4.
# The distance from 8 to 0 is |8| = 8.
# Thus, the closest number to 0 in the array is 1.
# Example 2:

# Input: nums = [2,-1,1]

# Output: 1
# Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
 

# Constraints:

# 1 <= n <= 1000
# -105 <= nums[i] <= 105

# Time complexity: O(n)
# Space complexity: O(1)
from typing import List

def findClosestNumber(nums: List[int]) -> int:
    closest = nums[0]
    for n in nums:
        if n == closest or abs(n) < abs(closest):
            closest = n

        elif abs(n) == abs(closest):
            closest = abs(n)

    return closest

# input: [-4,-2,1,4,8]
# expected: 1
print(findClosestNumber([-4,-2,1,4,8]))

# input: [2,-1,1]
# expected: 1
print(findClosestNumber([-4,-2,1,4,8]))

# input: [-100000,-100000]
# expected: -100000
print(findClosestNumber([-100000,-100000]))