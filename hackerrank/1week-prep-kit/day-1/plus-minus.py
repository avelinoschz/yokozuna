# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Example
# arr = [1, 1, 0, -1, -1]
# There are n = 5 elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.400000, 2/5 = 0.400000, and 1/5 = 0.200000. Results are printed as:
# 0.400000
# 0.400000
# 0.200000

# Function Description
# Complete the plusMinus function in the editor below.
# plusMinus has the following parameter(s):
# int arr[n]: an array of integers

# Print
# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 6 digits after the decimal. The function should not return a value.

# Input Format
# The first line contains an integer, n, the size of the array.
# The second line contains  space-separated integers that describe .

# Output Format
# Print the following 3 lines, each to 6 decimals:
# proportion of positive values
# proportion of negative values
# proportion of zeros

# Sample Input
# STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

# Sample Output
# 0.500000
# 0.333333
# 0.166667


def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    for num in arr:
        if num == 0:
            zer += 1
        elif num < 0:
            neg += 1
        else:
            pos += 1
            
    total = len(arr)
    print(pos/total)
    print(neg/total)
    print(zer/total)

# Sample test case 1
input1 = [-4, 3, -9, 0, 4, 1]
plusMinus(input1)

# Expected output 1:
# 0.500000
# 0.333333
# 0.166667

print("------------------------------")

# Sample test case 2
input2 = [1, 2, 3, -1, -2, -3, 0, 0]
plusMinus(input2)

# Expected output 2:
# 0.375000
# 0.375000
# 0.250000


