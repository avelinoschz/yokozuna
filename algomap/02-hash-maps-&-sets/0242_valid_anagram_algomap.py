# 0242. Valid Anagram

# https://algomap.io/problems/valid-anagram
# https://www.youtube.com/watch?v=_cCTcPQik6A

# Hash Maps & Sets

# Detailed Explanation

# Understanding the Problem: Valid Anagram

# The “Valid Anagram” problem is a classic string question that asks whether two given strings, s and t, are anagrams of each other. 
# Two strings are considered anagrams if they contain the exact same characters with the exact same frequencies, though possibly in a different order.

# For example:

# s = "anagram", t = "nagaram" → Output: true
# s = "rat", t = "car" → Output: false
# Why This Problem Matters

# Validating anagrams appears in problems involving string normalization, word frequency comparison, and even in applications like plagiarism detection or cryptography. 
# It reinforces core concepts in character counting and hash-based comparison.

# Brute Force Approach: Compare Frequency Dictionaries

# The most intuitive solution is to count the frequency of characters in both strings and compare the results. This is easily done using a Counter (or a hash map) for each string.

# Steps:

# Check Lengths: If the lengths of s and t differ, return false immediately.
# Count Characters: Use a frequency map to count characters in both s and t.
# Compare Maps: If the two frequency maps are equal, return true; otherwise, return false.
# Example Walkthrough

# Input: s = "listen", t = "silent"

# Frequency of s: {l:1, i:1, s:1, t:1, e:1, n:1}
# Frequency of t: {s:1, i:1, l:1, e:1, n:1, t:1}
# Maps are equal → return true
# Optimized Alternative: Sort and Compare

# An equally valid solution is to sort both strings and compare the results. If the sorted versions of s and t match, then they must be anagrams.

# s = "anagram" → sorted(s) = "aaagmnr"
# t = "nagaram" → sorted(t) = "aaagmnr"
# Match → return true
# Time Complexity: O(n log n), due to sorting.

# Time and Space Complexity

# Using Counters:
# Time Complexity: O(n), where n is the length of the strings.
# Space Complexity: O(1), because we use at most 26 letters (if constrained to lowercase English).

# Using Sorting:
# Time Complexity: O(n log n)
# Space Complexity: O(n) due to the creation of sorted copies.

# Edge Cases to Consider

# Different lengths → immediately return false
# Empty strings → return true (two empty strings are trivially anagrams)
# Case sensitivity → "a" and "A" are not the same
# Whitespace or punctuation → consider problem constraints before handling
# Conclusion

# The “Valid Anagram” problem is simple but powerful. It demonstrates how to solve problems by counting frequency or sorting structures. 
# Mastering both approaches sharpens your skills in working with strings and hash maps—critical tools in programming and algorithm design.

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = Counter(s)
        dict_t = Counter(t)

        return dict_s == dict_t

# Let n be the length of the longest word
# Time complexity: O(n)
# Space complexity: O(n)