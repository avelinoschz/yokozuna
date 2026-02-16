# 20. Valid Parentheses

# Neetcode video solution
# https://www.youtube.com/watch?v=WTzjTskDFMg

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

# Original neetcode solution
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