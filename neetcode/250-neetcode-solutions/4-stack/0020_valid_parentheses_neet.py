# 20. Valid Parentheses

# Topic: Stack

# Question: https://neetcode.io/problems/validate-parentheses/question

# Neetcode video solution: https://www.youtube.com/watch?v=WTzjTskDFMg

# Difficulty: Easy

# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true
# Example 3:

# Input: s = "[(])"

# Output: false
# Explanation: The brackets are not closed in the correct order.

# Constraints:

# 1 <= s.length <= 1000

# Time complexity: O(n)
# Space complexity: O(n)

# 1. Brute Force
# The idea is simple:
# valid parentheses must always appear in matching pairs like "()", "{}", or "[]".
# So if the string is valid, we can repeatedly remove these matching pairs until nothing is left.
# If, after removing all possible pairs, the string becomes empty, then the parentheses were properly matched.
# Otherwise, some unmatched characters remain, meaning the string is invalid.

# Time complexity: O(n^2)
# Space complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''

# 2. Stack
# Valid parentheses must follow a last-opened, first-closed order — just like stacking plates.
# So we use a stack to track opening brackets.
# Whenever we see a closing bracket, we simply check whether it matches the most recent opening bracket on top of the stack.
# If it matches, we remove that opening bracket.
# If it doesn't match (or the stack is empty), the string is invalid.
# A valid string ends with an empty stack.

# Time complexity: O(n)
# Space complexity: O(n)

# Original neetcode solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

# Refactored Neetcode soluton with some changes to make it more readable and easier to understand
def isValid(s):
    stack = []
    pairs = {
        ')': '(',
        '}':'{',
        ']':'['
    }
    
    for c in s:
        if stack and c in pairs:
            if stack[-1] == pairs[c]:
                stack.pop()
            else:
                return False

        else:
            stack.append(c)

    return len(stack) == 0


s = "(}"
result = isValid(s)
print(f"input: {s} | output: {result}")
print("pass: ", result == True)

s = "()[]{}"
result = isValid(s)
print(f"input: {s} | output: {result}")
print("pass: ", result == True)

s = "(]"
result = isValid(s)
print(f"input: {s} | output: {result}")
print("pass: ", result == False)

s = "(("
result = isValid(s)
print(f"input: {s} | output: {result}")
print("pass: ", result == False)

s = "){"
result = isValid(s)
print(f"input: {s} | output: {result}")
print("pass: ", result == False)

s = "([]"
result = isValid(s)
print(f"input: {s} | output: {result}")
print("pass: ", result == False)