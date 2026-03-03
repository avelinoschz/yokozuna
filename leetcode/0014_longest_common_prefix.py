# 14. Longest Common Prefix

# https://leetcode.com/problems/longest-common-prefix/description/

# Easy

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.


# First try before looking at the solution.
# Time complexity: O(n*m) where n is the number of strings and m is the length of the longest common prefix
# Time complexity: O(n) Another way to formulate is where n is the sum of the lengths of all strings in the array.
# Space complexity: O(1)

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    base_word = strs[0]
    prefix = 0
    for c in base_word:
        for w in strs[1:]:
            if not w or prefix >= len(w) or c != w[prefix]:
                return base_word[:prefix]

        prefix += 1

    return base_word

strs = ["flower","flow","flight"]
result = longestCommonPrefix(strs)
print("result:", result)
print("expected:", "fl")

