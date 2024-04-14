# https://www.hackerrank.com/challenges/three-month-preparation-kit-divisible-sum-pairs/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

# Given an array of integers and a positive integer `k`, determine the 
# number of (i,j) pairs where i < j and ar[i] + ar[j] is divisible by `k`.

# Example
# ar = [1,2,3,4,5,6]
# k = 5

# Three pairs meet the criteria: [1,4], [2,4] and [4,6].

# Function Description
# Complete the divisibleSumPairs function in the editor below.
# divisibleSumPairs has the following parameter(s):
# int n: the length of array `ar`
# int ar[n]: an array of integers
# int k: the integer divisor

# Returns
# - int: the number of pairs

# Input Format
# The first line contains 2 space-separated integers, `n` and `k`.
# The second line contains `n` space-separated integers, each a value of `arr[i]`.

# Sample Input
# STDIN           Function
# -----           --------
# 6 3             n = 6, k = 3
# 1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]
# Sample Output
# 5

# First try, using brute-force approach
# O(n^2) time | O(1) space
def divisibleSumPairs1(n, k, ar):
    divisible_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            pair_sum = ar[i] + ar[j]
            if (pair_sum % k) == 0:
                print("pair:",  ar[i], ar[j])
                divisible_pairs += 1
        
    return divisible_pairs

# After searching for a better solution
# And using ChatGPT too

# The solution is based on complementing the remainders.
# e.g. k = 3
# 10 % 3 = 1
# This means that 10 + any number that has a remainder of 2
# will satisfy the condition of a sum pair being multiple of 3
# Like: 17 % 3 = 2
# 10 + 17 = 27 % 3 = 0

# Then the solution is counting the remainders frequency.
# Let's say 10, 19, 28; are all numbers with remainder 1
# And 17, 23, 32, 65; are all numbers with remainder 2
# Meaning that all the possible sums between numbers
# with remainder 1 and remainder 2, would be the solution.
# 10 + 17; 10 + 23; 10 + 32; 10 + 65
# 19 + 17; 19 + 23; 19 + 32; 19 + 65
# 28 + 17; 28 + 23; 28 + 32; 28 + 65
# Therefore, 12

# O(n) time | O(n) space
def divisibleSumPairs2(n, k, ar):
    remainders_freq = {}
    count = 0

    for num in ar:
        print("num:", num)
        remainder = num % k
        complement = (k - remainder) % k
        print("remainder:", remainder)
        print("complement:", complement)

        print("count before", count)
        if complement in remainders_freq:
            count += remainders_freq[complement]
        print("count after", count)
        print("---------")

        remainders_freq[remainder] = remainders_freq.get(remainder, 0) + 1

    print(remainders_freq)

    return count

# ar = [1,2,3,4,5,6]
# k = 5
# expected = [[1,4],[2,3],[4,6]]
# print(result == len(expected))

# ar = [1, 3, 2, 6, 1, 2]
# k = 3
# expected = [[1,2],[1,2],[3,6],[2,1],[1,2]]
# print(result == len(expected))

# ar = [1, 2, 15, 33, 60, 100]
# k = 3
# expected = [[1,2], [2, 100], [15,33], [15, 60], [33, 60]]
# print(result == len(expected))

ar = [10, 17, 19, 23, 28, 32, 65]
k = 3
expected = 12
result = divisibleSumPairs2(len(ar), k, ar)
print("result:", result)
print(result == expected)