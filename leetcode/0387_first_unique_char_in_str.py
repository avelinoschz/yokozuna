# 387. First Unique Character in String

# https://leetcode.com/problems/first-unique-character-in-a-string/

# Easy

# Given a string `s``, find the first non-repeating character in it and 
# return its index. If it does not exist, return `-1``.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

# Time complexity: O(n+n), therefore, O(n) 
# Space complexity: O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
            
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        
        return -1
            