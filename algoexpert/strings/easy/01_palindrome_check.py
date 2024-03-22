# https://www.algoexpert.io/questions/palindrome-check

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

# Solution using a reversed for loop and concatanation
# O(n) time | O(n) space
def isPalindrome(string):
    pal = ''
    for i in reversed(range(len(string))):
    # for i in range(len(string)-1, -1, -1):
        pal += string[i]

    return string == pal

# Solution using two pointers over the string
# O(n) time | O(1) space
def isPalindrome(string):
    l, r = 0, len(string)-1
    while l <= r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True

# Solution using recursion
# O(n/2) therefore O(n) time | O(n/2) therefore O(n) space
def isPalindrome(string):
    if not string or len(string)==1:
        return True

    if string[0] == string[-1]:
        return isPalindrome(string[1:-1])

    else:
        return False


string = "abcddcba"
result = isPalindrome(string)
print(result)