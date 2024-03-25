# 155. Min Stack

# neetcode video solution
# https://www.youtube.com/watch?v=qkLl7nAwDPo

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
