# 20. Valid Parentheses

# neetcode video solution
# https://www.youtube.com/watch?v=WTzjTskDFMg

# Time complexity: O(n)
# Space complexity: O(n)

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    pairs = {
        ')': '(',
        '}':'{',
        ']':'['
    }

    # Original neetcode solution
    # for c in s:
    #     if c in pairs:
    #         if stack and stack[-1] == pairs[c]:
    #             stack.pop()
    #         else:
    #             return False

    #     else:
    #         stack.append(c)

    # return True if not stack else False 

    # This is my way, for me better to understand what is happening
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