# 1768. Merge Strings Alternately

# https://neetcode.io/problems/merge-strings-alternately/question
# https://www.youtube.com/watch?v=LECWOvTo-Sc

# Easy

# You are given two strings, word1 and word2. Construct a new string by merging them in alternating order, starting with word1 — take one character from word1, then one from word2, and repeat this process.

# If one string is longer than the other, append the remaining characters from the longer string to the end of the merged result.

# Return the final merged string.

# Example 1:

# Input: word1 = "abc", word2 = "xyz"

# Output: "axbycz"
# Example 2:

# Input: word1 = "ab", word2 = "abbxxc"

# Output: "aabbbxxc"
# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

# 1. Two Pointers - I
# We want to interleave characters from both strings, taking one from each in turn. Using two pointers, we can walk through both strings simultaneously. 
# While both strings have characters remaining, we append one from each. Once one string is exhausted, we append whatever remains from the other string.

# Time complexity: O(n+m)
# Space complexity: O(n+m) for the output string.
# Where n and m are the lengths of the strings word1 and word2 respectively.
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
    
# 2. Two Pointers - II
# Instead of handling the remaining characters separately after the main loop, we can continue the loop as long as either string has characters left. 
# In each iteration, we check if each pointer is still valid before appending. This approach handles unequal length strings naturally within a single loop.

# Time complexity: O(n+m)
# Space complexity: O(n+m) for the output string.
# Where n and m are the lengths of the strings word1 and word2 respectively.
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        res = []
        i = j = 0
        while i < n or j < m:
            if i < n:
                res.append(word1[i])
            if j < m:
                res.append(word2[j])
            i += 1
            j += 1
        return "".join(res)
    
# 3. One Pointer
# Since we always process characters at the same index from both strings in each iteration, we can simplify to a single index variable. 
# We iterate up to the length of the longer string, and for each index, we add the character from each string if that index is valid.

# Time complexity: O(n+m)
# Space complexity: O(n+m) for the output string.
# Where n and m are the lengths of the strings word1 and word2 respectively.
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        res = []
        for i in range(max(m, n)):
            if i < n:
                res.append(word1[i])
            if i < m:
                res.append(word2[i])
        return "".join(res)