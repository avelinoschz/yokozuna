# 20. Valid Parentheses

# https://leetcode.com/problems/valid-parentheses/

# Difficulty: Easy

# Given a string s containing just the characters 
# '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Time complexity: O(n)
# Space complexity: O(n)

# Last iteration after looking at better solutions. First solutions are at the bottom.
# This covers all cases with a more simple solution
def isValid(s):
    stack = []
    pairs = {
        '(': ')',
        '{':'}',
        '[':']'
    }

    for bracket in s:
        # if it's an opening we add it to the stack
        if bracket in pairs:
            stack.append(bracket)
        
        # if len is 0, means we found a closing bracket as first character: invalid
        # if the bracket is diff from the closing of the popped one: invalid
        elif len(stack) == 0 or bracket != pairs[stack.pop()]:
            return False

    # if len is differente than 0 means we have unclosed brackets
    # for example, if we only have 1 opening bracket as the input
    return len(stack) == 0


s = "()"
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

s = "[[[]"
result = isValid(s)
print(f"input: {s} | output: {result}")
print("pass: ", result == False)

# This solves a simple case were all parentheses are always together
# Like ()[](). But needs some changes if they could be nested.
# def isValid(s):
#     for i in range(0, len(s), 2):
#         if s[i] == "(" and s[i+1] == ")":
#             continue

#         elif s[i] == "[" and s[i+1] == "]":
#             continue

#         elif s[i] == "{" and s[i+1] == "}":
#             continue

#         else:
#             return False

#     return True


# This is the second iteration of the problem, considering nested parentheses
# def isValid(s):
#     if len(s) <= 1:
#         return False

#     if len(s)%2 != 0:
#         return False

#     stack = []
#     for i in range(0, len(s)):
#         if len(stack) > 1 and i == len(s)-1:
#             return False

#         if s[i] == '(' or s[i] == '[' or s[i] == '{':
#             if i == len(s)-1:
#                 return False
#             stack.append(s[i])

#         elif s[i] == ')':
#             if len(stack) == 0:
#                 return False
#             pop = stack.pop()
#             if pop != '(':
#                 return False

#         elif s[i] == ']':
#             if len(stack) == 0:
#                 return False
#             pop = stack.pop()
#             if pop != '[':
#                 return False

#         elif s[i] == '}':
#             if len(stack) == 0:
#                 return False
#             pop = stack.pop()
#             if pop != '{':
#                 return False

#         else:
#             return False


#     return True