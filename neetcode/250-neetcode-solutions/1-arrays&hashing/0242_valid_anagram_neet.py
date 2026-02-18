# 242. Valid Anagram

# Topic: Arrays & Hashing

# Neetcode video solution
# https://www.youtube.com/watch?v=9UtInBqnCgA

# Difficulty: Easy

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.

# 1. Sorting
# If two strings are anagrams, they must contain exactly the same characters with the same frequencies.
# By sorting both strings, all characters will be arranged in a consistent order.
# If the two sorted strings are identical, then every character and its count match, which means the strings are anagrams.

# Time & Space Complexity
# Time complexity: O(nlogn+mlogm)
# Space complexity: O(n+m) depending on the sorting algorithm.
# Where n is the length of string s and m is the length of string t.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    
# 2. Hash Map
# If two strings are anagrams, they must use the same characters with the same frequencies.
# Instead of sorting, we can count how many times each character appears in both strings.
# By using two hash maps (or dictionaries), we track the frequency of every character in each string.
# If both frequency maps match exactly, then the strings contain the same characters with same frequencies, meaning they are anagrams.

# Time complexity: O(n+m)
# Space complexity: O(1) since we have at most 26 different characters.
# Where n is the length of string s and m is the length of string t.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
# 3. Hash Table (Using Array)
# Since the problem guarantees lowercase English letters, we can use a fixed-size array of length 26 to count character frequencies instead of a hash map.
# As we iterate through both strings simultaneously, we increment the count for each character in s and decrement the count for each character in t.
# If the strings are anagrams, every increment will be matched by a corresponding decrement, and all values in the array will end at 0.
# This approach is efficient because it avoids hashing and uses constant space.

# Time complexity: O(n+m)
# Space complexity: O(1) since we have at most 26 different characters.
# Where n is the length of string s and m is the length of string t.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True