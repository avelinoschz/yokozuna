# 0017. Roman to Integer

# https://algomap.io/problems/roman-to-integer
# https://www.youtube.com/watch?v=VYqQeKj3a2

# Arrays & Strings

# Detailed Explanation

# Problem Overview

# The Roman to Integer problem requires us to take a string made up of Roman numeral characters and convert it into its corresponding integer value. 
# Roman numerals were used in ancient Rome and are built using specific letters that represent fixed values. 
# The challenge lies in not only interpreting each symbol but also understanding when to subtract values instead of adding them.

# Understanding Roman Numerals

# There are seven Roman numeral symbols, each associated with a specific integer: I is 1, V is 5, X is 10, L is 50, C is 100, D is 500, and M is 1000. 
# In most cases, you add the values of these symbols from left to right. For example, the numeral "VIII" is read as 5 + 1 + 1 + 1 = 8.

# However, Roman numerals also allow for a subtractive notation. This occurs when a smaller numeral appears before a larger one, indicating that the smaller value should be subtracted from the larger. 
# For instance, "IV" is 4, because 1 comes before 5, and "IX" is 9, because 1 comes before 10. This rule applies specifically to six cases: "IV" (4), "IX" (9), "XL" (40), "XC" (90), "CD" (400), and "CM" (900).

# How the Algorithm Works

# To convert a Roman numeral to an integer, we process the string from left to right. For each character, we look at its value using a fixed mapping. 
# If the character is followed by one of greater value, we interpret the two as a subtractive pair and subtract the current value from the next, adding the result to our running total. 
# After processing such a pair, we skip the next character since it's already been handled. Otherwise, if the next character is smaller or equal, we simply add the current character’s value to the result.

# For example, if we encounter "C" followed by "M", we recognize that 100 comes before 1000, and so we compute 1000 - 100 = 900 and add that to the total. 
# We then move ahead by two characters to continue the scan.

# Example Walkthrough

# Let's walk through the input "MCMXCIV", which is a common test case:

# - The first character is "M", which equals 1000. We add 1000 to the total.
# - The next two characters are "C" and "M". Since C is less than M, we recognize the subtractive pair CM, which equals 900. We add 900.
# - We then move to "X" and "C". Again, X is less than C, so this is another subtractive case: 100 - 10 = 90. We add 90.
# - Finally, we encounter "I" and "V". Since I is less than V, we compute 5 - 1 = 4 and add that to the total.

# Putting it all together: 1000 + 900 + 90 + 4 = 1994.

# Time and Space Complexity

# The algorithm runs in linear time relative to the length of the input string, so the time complexity is O(n). 
# This is because each character is processed at most once. The space complexity is O(1), since the character-to-value mapping is fixed and constant, and no additional data structures grow with input size.

# Summary

# Converting Roman numerals to integers is a classic string-parsing task that teaches control flow and pattern recognition. 
# The key idea is to recognize when a character should be added versus when it forms part of a subtractive pair with the next character. 
# With a simple mapping and a loop, this can be implemented efficiently and cleanly. The subtractive rules are the only subtlety, and once handled, the rest of the conversion is straightforward.

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        summ = 0
        n = len(s)
        i = 0
        
        while i < n:
            if i < n - 1 and d[s[i]] < d[s[i+1]]:
                summ += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                summ += d[s[i]]
                i += 1
        
        return summ
        # Time: O(n)
        # Space: O(1)
 
