# 217. Contains Duplicate

# neetcode video solution
# https://www.youtube.com/watch?v=3OamzN90kPg

# This problem has a couple of solutions:

# First one is done by just brute force.
# Iterate and compare all the possible combinations.
# This would be: O(n^2) time | O(1) space

# A second way to solve it, is by first sorting the list,
# and then search for adyacent duplicates.
# This would be: O(n log) time | O(1)
# This is not a so bad solution, has a better time complexity
# than first way, and has a good space usage.

# The third way is the one actually implemented, 
# trade off using more space, but getting a much more better
# time complexity. Depending on what we want to prioritize,
# 2nd or 3rd could be valid options.

from typing import List

# Time complexity: O(n)
# Space complexity: O(n)
def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)

    return False