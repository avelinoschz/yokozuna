# 242. Valid Anagram

# https://leetcode.com/problems/valid-anagram/description/

# Difficulty: Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters. 

# Super Pythonic solution
from collections import Counter

def isAnagram0(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# Solution 1: Hash Map
# Time complexity: O(n)
# Space complexity: O(n)
def isAnagram1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    word1 = {}
    word2 = {}

    for i in range(0, len(s)):
        c1 = s[i]
        if c1 not in word1:
            word1[c1] = 1
        else:
            word1[c1] += 1

        c2 = t[i]
        if c2 not in word2:
            word2[c2] = 1
        else:
            word2[c2] += 1

    return word1 == word2

# Alternative solution 1, doing manual check
def isAnagram12(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count_s, count_t = {}, {}

    for i in range(0, len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[t[i]] = count_t.get(t[i], 0) + 1

    for c in count_s:
        if count_s[c] != count_t.get(c, 0):
            return False
                    
    return True

# Solution 2: Sorting
# Time complexity: O(n log n) due to sorting
# Space complexity: O(1) if we ignore the space used by sorting, otherwise O(n) due to the space used by the sorted strings.
def isAnagram2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Solution 3: Frequency array
# Time complexity: O(n)
# Space complexity: O(1) since we have at most 26 different characters.
def isAnagram3(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    freq_s = [0] * 26
    freq_t = [0] * 26

    for i in range(0, len(s)):
        freq_s[ord(s[i]) - ord('a')] += 1
        freq_t[ord(t[i]) - ord('a')] += 1

    return freq_s == freq_t

input1 = "anagram"
input2 = "nagaram"
print(isAnagram0(input1, input2))


        