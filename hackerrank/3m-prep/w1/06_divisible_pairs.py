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
def divisibleSumPairs(n, k, ar):
    divisible_pairs = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            pair_sum = ar[i] + ar[j]
            if (pair_sum % k) == 0:
                divisible_pairs += 1
        
    return divisible_pairs