# 0049. Group Anagrams

# https://leetcode.com/problems/group-anagrams/description/

# Medium

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
 
from collections import defaultdict
from typing import List

# Hash map and hash table
# After looking at some solutions, and pythonic way to do stuff, I found out that we can use a frequency array as the key in a hash map, and the value is the list of anagrams. 
# This is more efficient than sorting the string every time we want to find the anagrams, because sorting takes O(nlogn) time, while creating the frequency array takes O(n) time.

# Time complexity: O(m*n)
# Space complexity:
# - O(m) extra space.
# - O(m*n) space for the output list.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            anagrams[tuple(count)].append(s)

        return list(anagrams.values())
    

# Sorting
# This was taken from the leetcode solutions tab and is not my original solution. But it is very similar to what I proposed in my first try, but in much more Pythonic way.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        
        return list(ans.values())
    
# My first trying to solve the problem. I thought about using a frequency array (or conceptually a hash set).
# I thought about using a map, but I didn't know some python specific, like how to use a tuple as key in a hash map, 
# so I used a list to store the frequency arrays and then I compared the frequency arrays to find the anagrams. This is not very efficient, but it works.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = []
        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1

            found = False
            for f in freq:
                if count == f:
                    found = True
                    break
            
            if not found:
                freq.append(count)
        
        anagrams = []
        for _ in range(0, len(freq)):
            anagrams.append([])

        for w in strs:
            count = [0] * 26
            for i in range(len(w)):
                count[ord(w[i]) - ord('a')] += 1
            
            for f in freq:
                if count == f:
                    anagrams[freq.index(f)].append(w)

        return anagrams
    
# Second try, I tried again with a hashmap, but this time I used the sorted string as the key, and the value is the index of the anagrams list where we will store the anagrams. 
# This is more efficient than the previous solution, but it is still not very efficient because we are sorting the string every time we want to find the anagrams. But it works.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        i = 0
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string not in words:
                words[sorted_string] = i
                i += 1

        anagrams = []
        for _ in range(0, len(words)):
            anagrams.append([])
        
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string in words:
                anagrams[words[sorted_string]].append(s)

        return anagrams