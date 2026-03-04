# 0017. Roman to Integer

# https://neetcode.io/problems/roman-to-integer/question
# https://www.youtube.com/watch?v=3jdxYj3DD98

# Math & Geometry

# Easy

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# You are given a roman numeral as a string s, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3

# Example 2:
# Input: s = "XLIX"
# Output: 49

# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

# 1. Hash Map
# Roman numerals normally add values from left to right. The key insight is handling subtractive notation, where a smaller value before a larger one means subtraction (like IV = 4, not 6). 
# As we scan left to right, if the current symbol is smaller than the next one, we subtract its value; otherwise, we add it. This single rule handles both regular addition and subtractive cases elegantly.

# Time complexity: O(n)
# Space complexity: O(1) since we have 7 characters in the hash map.
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res
