# 1929. Concatenation of Array

# Topic: Arrays & Hashing

# Neetcode video solution
# https://www.youtube.com/watch?v=68isPRHgcFQ

# Difficulty: Easy

# Time complexity: O(n + 2) which is O(n)
# Space complexity: O(n)

# You are given an integer array nums of length n. Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

# Example 1:

# Input: nums = [1,4,1,2]

# Output: [1,4,1,2,1,4,1,2]
# Example 2:

# Input: nums = [22,21,20,1]

# Output: [22,21,20,1,22,21,20,1]
# Constraints:

# 1 <= nums.length <= 1000.
# 1 <= nums[i] <= 1000

nums = [2,1,3]

# 1. Iteration (Two Pass)
# To concatenate an array with itself, we need to create a new array that contains all elements of the original array twice, maintaining the same order.
# The elements at indices 0 to n−1 are followed by the same elements at indices n to 2n−1.

# Time complexity: O(n) where n is the length of the input array. We iterate through the array twice, performing 2n operations.
# Space complexity: O(n) if we consider the space required for the output array of size 2n.
def getConcatenation(nums):
    ans = []
    for i in range(2):
        for num in nums:
            ans.append(num)
    return ans

# 2. Iteration (One Pass)
# The problem defines the result array ans such that ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n. 
# Instead of looping through the input twice, we can fill both required positions in the result array simultaneously while iterating through the input array just once. This utilizes the index mapping i and i + n directly.

# Time complexity: O(n) where n is the length of the input array. Although we iterate through the input once, we still perform 2n total writes to the output array.
# Space complexity: O(n) as we must allocate an array of size 2n for the output.
def getConcatenation2(nums):
    n = len(nums)
    ans = [0] * (2 * n)
    for i, num in enumerate(nums):
        ans[i] = ans[i + n] = num
    return ans