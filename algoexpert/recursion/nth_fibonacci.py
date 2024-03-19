# This was my first try sovling the problem using iterations
# One important part of the problem, is that the input `n` is index
# For example if n is 1, needs to return zero because is the first 
# number of the sequence. If input is 2, then result needs to be 1
# and so on.
# Time complexity: O(N)
# Space complexity: O(1)
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    prev = 0
    curr = 1
    for i in range(2, n):
        new_fib = prev + curr
        prev = curr
        curr = new_fib


    return new_fib

# Next try using recursion. Needed to adjust the base cases.
# Time complexity: O(2^n)
# Space complexity: O(n)
def getNthFib2(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    return getNthFib(n-1) + getNthFib(n-2)

# This is a recursive version, but using memoization(aka cache)
# This is from AlgoExpert solution video
def getNthFib_AlgoRecursive(n, memo={1: 0, 2: 1}):
    if not n in memo:
        memo[n] = getNthFib(n-1) + getNthFib(n-2)
        
    return memo[n]

# This is the iterative solution from AlgoExpert.
def getNthFib_AlgoIterative(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        next = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = next
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]

target = 7
result = getNthFib_AlgoIterative(target)
print("result:", result)
# [0, 1, 1, 2, 3, 5, 8]