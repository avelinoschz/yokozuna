# 374. Guess Number Higher or Lower

# https://leetcode.com/problems/guess-number-higher-or-lower/

# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked 
# is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# Example 1:
# Input: n = 10, pick = 6
# Output: 6

# Example 2:
# Input: n = 1, pick = 1
# Output: 1

# Example 3:
# Input: n = 2, pick = 1
# Output: 1
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# This wasn't provided. I made it up as an example in case of running the solution.
def guess(n):
    pick = 6
    if n > pick:
        return 1
    elif n < pick:
        return -1
    else:
        return 0

# Time complexity: O(log n) 
# where `n` is the range given, not the array as in standard binary search

# Space complexity: O(1)
def guessNumber(n: int) -> int:
    low, high = 1, n

    while low <= high:
        mid = (low+high) // 2
        if guess(mid) < 0: # num > pick
            high = mid - 1
        elif guess(mid) > 0: # num < pick
            low = mid + 1
        else:
            return mid

    return -1