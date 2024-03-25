# 682. Baseball Number

# neetcode video solution
# https://www.youtube.com/watch?v=Id_tqGdsZQI

# Time complexity: O(n)
# Space complexity: O(n)

ops = ["5","2","C","D","+"]

stack = []
for op in ops:
    if op == "+":
        stack.append(stack[-1] + stack[-2])

    elif op == "D":
        stack.append(stack[-1] * 2)

    elif op == "C":
        stack.pop()

    else:
        stack.append(int(op))

print(sum(stack))

# Input: ops = ["5","2","C","D","+"]
# Output: 30
