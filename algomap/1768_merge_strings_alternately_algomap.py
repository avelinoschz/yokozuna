# 1768. Merge Strings Alternately

# Detailed Explanation

# Problem Overview

# You are given two strings, word1 and word2. The task is to create a new string by merging characters alternately from each input. 
# You begin with the first character of word1, followed by the first character of word2, then the second from word1, and so on. 
# This continues until all characters from both strings are used. If one string is longer than the other, the remaining characters from the longer string are appended at the end.

# Intuition

# The main idea is to traverse both strings at the same time and combine corresponding characters. 
# This works easily if both strings are of the same length. But when one string is longer, you need to handle the remaining characters properly. 
# Python's built-in zip function stops at the shortest input, so it doesn't help when lengths differ. Instead, itertools.zip_longest is a better choice. 
# It lets you continue pairing characters even after one input ends, filling in the missing values with an empty string. This way, the merging process becomes uniform and safe.

# Step-by-Step Approach

# First, import the zip_longest function from Python’s itertools module. You then use it to pair each character from word1 and word2. 
# If one string is shorter, zip_longest fills in the gap with an empty string so the loop can continue without errors. 
# For every paired set of characters, concatenate them and build the merged result as a single combined string. 
# The final result is simply the join of all such pairs.

# Example Walkthrough

# Consider the input strings word1 = "Hello" and word2 = "World". You begin by combining 'H' from word1 and 'W' from word2, then 'e' and 'o', then 'l' and 'r', and so on. 
# The process continues until both words are exhausted. In this case, both strings are of equal length, so there is no need to deal with leftovers. 
# The combined result is "HWeorlld", formed by merging the characters in alternating order.

# Time and Space Complexity

# The time complexity of this approach is O(max(m, n)), where m and n are the lengths of word1 and word2. This is because each character from both strings is processed once. 
# The space complexity is also O(m + n) since the final merged string contains all characters from both inputs.

# Conclusion

# Merging two strings alternately is a fundamental exercise in string manipulation and parallel traversal. 
# Using zip_longest provides a clear and concise way to handle uneven string lengths while preserving alternating behavior. 
# It allows you to write an elegant and readable solution that works in all cases without special conditionals.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A, B = len(word1), len(word2)
        a, b = 0, 0
        s = []
 
        word = 1
        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a += 1
                word = 2
            else:
                s.append(word2[b])
                b += 1
                word = 1
        
        while a < A:
            s.append(word1[a])
            a += 1
        
        while b < B:
            s.append(word2[b])
            b += 1
        
        return ''.join(s)
        # Let A be the length of Word1
        # Let B be the length of Word2
        # Let T = A + B
        
        # Time: O(T)
        # Space: O(T)
 

 
 
