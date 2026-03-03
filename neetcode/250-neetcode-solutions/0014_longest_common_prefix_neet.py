# 14. Longest Common Prefix

# https://neetcode.io/problems/longest-common-prefix/question
# https://www.youtube.com/watch?v=0sWShKIJoo4

# Arrays & Hashing 
# Trie

# Easy

# You are given an array of strings strs. Return the longest common prefix of all the strings.

# If there is no longest common prefix, return an empty string "".

# Example 1:

# Input: strs = ["bat","bag","bank","band"]

# Output: "ba"
# Example 2:

# Input: strs = ["dance","dag","danger","damage"]

# Output: "da"
# Example 3:

# Input: strs = ["neet","feet"]

# Output: ""
# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] is made up of lowercase English letters if it is non-empty.

from typing import List

# 1. Horizontal Scanning

# Start with the first string as the initial prefix candidate. Then compare it with each subsequent string, shrinking the prefix to match only the common portion. 
# After processing all strings, what remains is the longest common prefix. The prefix can only shrink or stay the same as we go through more strings.

# Time complexity: O(n*m)
# Space complexity: O(1)
# Where n is the length of the shortest string and m is the number of strings.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix
    
# 2. Vertical Scanning

# Instead of comparing entire strings horizontally, we can compare characters column by column across all strings. 
# Check if all strings have the same character at position 0, then position 1, and so on. The moment we find a mismatch or reach the end of any string, we've found where the common prefix ends.

# Time complexity: O(n*m)
# Space complexity: O(1)
# Where n is the length of the shortest string and m is the number of strings.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
    
# 3. Sorting

# When strings are sorted lexicographically, the first and last strings in the sorted order are the most different from each other. 
# If these two extremes share a common prefix, then all strings in between must also share that same prefix. So we only need to compare the first and last strings after sorting.

# Time complexity: O(n*mlogm)
# Space complexity: O(1) or O(m) depending on the sorting algorithm.
# Where n is the length of the longest string and m is the number of strings.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]
    

# 4. Trie

# A Trie naturally represents all prefixes. We insert the shortest string into the trie, then query each other string against it. 
# For each string, we walk down the trie as far as characters match, tracking how deep we get. The minimum depth reached across all strings is the length of the longest common prefix.

# Time complexity: O(n*m)
# Space complexity: O(n)
# Where n is the length of the shortest string and m is the number of strings.
class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

    def lcp(self, word: str, prefixLen: int) -> int:
        node = self.root
        for i in range(min(len(word), prefixLen)):
            if word[i] not in node.children:
                return i
            node = node.children[word[i]]
        return min(len(word), prefixLen)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        mini = 0
        for i in range(1, len(strs)):
            if len(strs[mini]) > len(strs[i]):
                mini = i

        trie = Trie()
        trie.insert(strs[mini])
        prefixLen = len(strs[mini])
        for i in range(len(strs)):
            prefixLen = trie.lcp(strs[i], prefixLen)
        return strs[0][:prefixLen]