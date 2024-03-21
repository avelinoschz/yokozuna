# https://leetcode.com/problems/min-stack/

# Design a stack that supports push, pop, top, and retrieving the minimum 
# element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# This was the first approach, but the popping is no O(1)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1 or val < self.min:
            self.min = val

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        popped = self.stack[-1]
        self.stack = self.stack[:-1]
        if len(self.stack) == 1:
            self.min = self.stack[0]

        elif self.min == popped and len(self.stack) > 1:
            self.min = self.stack[0]
            for i in range(1, len(self.stack)):
                if self.stack[i] < self.min:
                    self.min = self.stack[i]


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
    
# after reading the hint, though of this other approach
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack = self.stack[:-1]
        self.min_stack = self.min_stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()