# Palindrome Check

# https://www.algoexpert.io/questions/palindrome-check

# Easy

# Write a function that takes in a non-empty string and that returns 
# a boolean representing whether the string is a palindrome.

# A palindrome is defined as a string that's written the same forward 
# and backward. Note that single-character strings are palindromes.

# Sample Input
# string = "abcdcba"

# Sample Output
# true // it's written the same forward and backward

# Most optimal
# O(n) time | O(1) space - where `n` is the length of the input string

# Only added this solution, because the other ones were basically the same
# as what I already coded.
def isPalindrome_Algo(string, i = 0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome_Algo(string, i+1)

# optimized for tail recursion
def isPalindrome_Algo(string, i = 0):
    j = len(string) - 1 - i
    if i >= j:
        return True
    
    if string[i] == string[j]:
        return isPalindrome_Algo(string, i+1)

# -----------------------------------------------

# Solution using a reversed for loop and concatanation
# O(n^2) time | O(n) space
# The time complexity being n^2 is because how the string concatenation works.
# The operation of creating a new string is O(n), since we need to store all
# the characters in a new array of length `n`.
def isPalindrome(string):
    reversed = ''
    for i in range(len(string)-1, -1, -1):
        reversed += string[i]

    return string == reversed

# Another way, is instead of concatenate, is using and then join at the end
# to generate the comparison string
# O(n) time | O(n) space
def isPalindrome(string):
    reversed = []
    for i in reversed(range(len(string))):
        reversed.append(string[i])

    return string == ''.join(reversed)

# Solution using recursion
# O(n/2) therefore O(n) time | O(n/2) therefore O(n) space
def isPalindrome(string):
    if not string or len(string)==1:
        return True

    elif string[0] == string[-1]:
        return isPalindrome(string[1:-1])

    else:
        return False
    
# Another way of achieving the same result, using recursion
# inspared by AlgoExpert solution is the following one:
def isPalindrome(string):
    if not string or len(string)==1:
        return True

    return string[0] == string[-1] and isPalindrome(string[1:-1])

# Solution using two pointers over the string
# O(n/2) therefore O(n) time | O(1) space
def isPalindrome(string):
    l, r = 0, len(string)-1
    while l <= r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True

string = "abcddcba"
result = isPalindrome(string)
print(result)