# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:
# 1 2 3
# 4 5 6
# 9 8 9  

# The left-to-right diagonal 1 + 5 + 9 = 15 . The right to left diagonal 3 + 5 + 9 = 17. Their absolute difference is | 15 - 17 | = 2.

# Function description
# Complete the diagonalDifference function in the editor below.
# diagonalDifference takes the following parameter:
# int arr[n][m]: an array of integers

# Return
# int: the absolute diagonal difference

# Input Format
# The first line contains a single integer, n, the number of rows and columns in the square matrix arr.
# Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].
def diagonalDifference(arr):
    d1sum = 0
    d2sum = 0
    
    d1pos = 0
    d2pos = len(arr)-1

    for row in arr:
        d1sum += row[d1pos]
        d2sum += row[d2pos]
        d1pos += 1
        d2pos -= 1
            
    return abs(d1sum - d2sum)

matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10,8,-12]
]

print(diagonalDifference(matrix))

# Input (stdin)
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# Expected Output
# 15
