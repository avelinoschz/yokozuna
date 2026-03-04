# 0049. Group Anagrams

# https://algomap.io/problems/group-anagrams
# https://www.youtube.com/watch?v=eDmxPfVa81k

# Hash Maps & Sets

# Detailed Explanation

# Understanding the Problem: Group Anagrams

# The “Group Anagrams” problem asks you to group strings that are anagrams of each other. 
# Two strings are anagrams if they contain the same characters in any order, with the same frequency.

# For example, given the input ["eat", "tea", "tan", "ate", "nat", "bat"], the output should be grouped as:

# ["eat", "tea", "ate"]
# ["tan", "nat"]
# ["bat"]
# Why This Problem Matters

# This problem is widely used to teach the power of hashing and the idea of transforming complex objects into simpler keys. 
# It sharpens your understanding of how to efficiently group data based on custom equivalence logic and is foundational for problems involving classification, normalization, or frequency-based analysis.

# Basic Approach: Sort and Group

# The simplest way to group anagrams is by sorting each word and using the sorted result as the key. 
# All anagrams, once sorted, will yield the same string. For example:

# "eat" → "aet"
# "tea" → "aet"
# "ate" → "aet"
# These will all be grouped under the key "aet".

# Steps:

# Initialize an empty dictionary anagramGroups.
# For each word in the input list:
# Sort the characters in the word (O(K log K), where K is the word length).
# Use the sorted string as the key in the dictionary.
# Append the original word to the value list of that key.
# Return all value lists from the dictionary.
# Optimization: Use Letter Frequency Instead of Sorting

# Sorting each string costs O(K log K), which can be slow for large K. 
# Instead, we can use a frequency count of characters (like a 26-element array for lowercase English letters).

# Steps:

# Initialize an empty dictionary anagramGroups.
# For each string:
# Create a frequency count (array of 26 zeros).
# Increment the count for each character in the word.
# Convert the array to a tuple (since lists aren't hashable) and use that as the key.
# Append the word to the group corresponding to that key.
# Return all grouped values.
# Efficiency Gain:

# Instead of sorting, counting characters takes O(K) per word. 
# This reduces the overall time complexity from O(NK log K) to O(NK), where N is the number of words.

# Example Walkthrough

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Using sorted strings:

# "eat" → "aet"
# "tea" → "aet"
# "tan" → "ant"
# "ate" → "aet"
# "nat" → "ant"
# "bat" → "abt"
# Final groups:

# ["eat", "tea", "ate"]
# ["tan", "nat"]
# ["bat"]

# Time and Space Complexity

# Time Complexity:

# Using sorting: O(NK log K)
# Using frequency counting: O(NK)
# Space Complexity: O(NK), since we store N strings each of length up to K, and the dictionary stores grouping information.
# Edge Cases to Consider

# Empty input list → return []
# All strings are identical → one group
# All strings are unique with no anagrams → each string in its own group

# Conclusion

# The “Group Anagrams” problem is a powerful example of classification and grouping using hash maps. 
# It reinforces strategies like character counting and normalization, which are frequently useful in both algorithm design and data preprocessing tasks in the real world.

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs: # n
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            anagrams_dict[key].append(s)
 
        return anagrams_dict.values()
# n is the number of strings, m is the length of largest string
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
 
