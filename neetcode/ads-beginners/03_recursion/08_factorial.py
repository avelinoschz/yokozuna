# This is a factorial done with a loop
# def factorial(n):
#     times = n
#     for i in range(n-1, 0, -1):
#         times *= i
#     return times

# num = 5
# result = factorial(num)
# print(result)

# Time complexity: O(n)
# Space complexity: O(n)
def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n-1)

num = 5
result = factorial_recursive(num)
print(result)