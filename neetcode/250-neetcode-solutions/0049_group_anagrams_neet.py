# 49. Group Anagrams

# https://neetcode.io/problems/anagram-groups/question
# https://www.youtube.com/watch?v=vzdNOK2oB2E

# Medium

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# 1. Sorting
# Anagrams become identical when their characters are sorted.
# For example, "eat", "tea", and "ate" all become "aet" after sorting.
# By using the sorted version of each string as a key, we can group all anagrams together.
# Strings that share the same sorted form must be anagrams, so placing them in the same group is both natural and efficient.

# Time complexity: O(m*nlogn)
# Space complexity: O(m*n)
# Where m is the number of strings and n is the length of the longest string.
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())   
    

# 2. Hash Table
# Instead of sorting each string, we can represent every string by the frequency of its characters.
# Since the problem uses lowercase English letters, a fixed-size array of length 26 can capture how many times each character appears.
# Two strings are anagrams if and only if their frequency arrays are identical.
# By using this frequency array (converted to a tuple so it can be a dictionary key), we can group all strings that share the same character counts.

# Time complexity: O(m*n)
# Space complexity:
# - O(m) extra space.
# - O(m*n) space for the output list.
# Where m is the number of strings and n is the length of the longest string.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

