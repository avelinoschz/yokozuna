# This was my first try, before looking at the sol video
# def fibonacci(n):
#     if n == 0:
#         return 0
    
#     if n == 1:
#         return 1
    
#     res = fibonacci(n-1) + fibonacci(n-2)
#     return res

# Time complexity: O(2^n)
# Space complexity: O(n)
def fibonacci(n):
    if n <= 1:
        return n
    
    res = fibonacci(n-1) + fibonacci(n-2)
    return res

def fibonacci_loop(n):
    prev = 0
    curr = 1
    i = 2
    while i <= n:
        fib = curr + prev
        prev = curr
        curr = fib
        i += 1
    return fib

n = 6
result = fibonacci(n)
print(result)

# f(0) = 0
# f(1) = 1

# f(n) = f(n-1) + f(n-2)
# f(2) = f(1) + f(0)
# f(2) = 1 + 0 = 1

# f(3) = f(2) + f(1)
# f(3) = 1 + 1 = 2
# f(4) = 2 + 1 = 3
# f(5) = 3 + 2 = 5
# f(6) = 5 + 3 = 8
# 0 1 1 2 3 5 8 