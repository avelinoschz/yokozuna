# 155. Min Stack

# Neetcode video solution
# https://www.youtube.com/watch?v=qkLl7nAwDPo

# Difficulty: Medium

# Design a stack class that supports the push, pop, top, and getMin operations.

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in O(1) time.

# Example 1:
# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

# Output: [null,null,null,null,0,null,2,1]

# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(1);
# minStack.push(2);
# minStack.push(0);
# minStack.getMin(); // return 0
# minStack.pop();
# minStack.top();    // return 2
# minStack.getMin(); // return 1

# Constraints:
# -2^31 <= val <= 2^31 - 1.
# pop, top and getMin will always be called on non-empty stacks.

class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []
     
    def push(self, val) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
         
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    
# Your MinStack object will be instantiated and called as such:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
min = min_stack.getMin() # return -3
print(min)
min_stack.pop()
top = min_stack.top() #return 0
print(top)
min = min_stack.getMin() # return -2
print(min)
print("stack:", min_stack.stack)
print("min_stack:", min_stack.min_stack)
