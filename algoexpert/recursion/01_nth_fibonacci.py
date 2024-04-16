# Nth Fibonacci

# https://www.algoexpert.io/questions/nth-fibonacci

# Easy

# The Fibonacci sequence is defined as follows: the first number of the 
# sequence is `0`, the second number is `1`, and the nth number is the sum 
# of the (n - 1)th and (n - 2)th numbers.

# Write a function that takes in an integer `n` and returns the nth Fibonacci number.

# Important note: the Fibonacci sequence is often defined with its first two numbers as
# `FO = 0` and `F1 = 1`. For the purpose of this question, the first Fibonacci number is
# `FO`; therefore,` getNthFib(1)` is equalto `FO`, `getNthFib(2)` is equalto `F1`, etc..

# Sample Input #1
# n = 2

# Sample Output #1
# 1 // 0, 1

# Sample Input #2
# n = 6

# Sample Output #2
# 5 // 11 0, 1, 1, 2, 3,

# This is a recursive version, but using memoization(aka cache)
# This is from AlgoExpert solution video

# O(n^2) time | O(n) space - where n is the input number
def getNthFib_Algo1(n, memo={1: 0, 2: 1}):
    if not n in memo:
        memo[n] = getNthFib_Algo1(n-1) + getNthFib_Algo1(n-2)
        
    return memo[n]

# This is the iterative solution from AlgoExpert.

# O(n) time | O(1) space - where n is the input number
def getNthFib_Algo2(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        next = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = next
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]

# -----------------------------------------------
# This was my first try sovling the problem using iterations
# One important part of the problem, is that the input `n` is index
# For example if n is 1, needs to return zero because is the first 
# number of the sequence. If input is 2, then result needs to be 1
# and so on.

# Time complexity: O(n)
# Space complexity: O(1)
def getNthFib1(n):
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

    return getNthFib2(n-1) + getNthFib2(n-2)

target = 7
result = getNthFib_Algo2(target)
print("result:", result)
# [0, 1, 1, 2, 3, 5, 8]