# Sean invented a game involving a 2n x 2n matrix where each cell of the matrix contains an integer. He
# can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum
# of the elements in n x n the submatrix located in the upper-left quadrant of the matrix.

# Given the initial configurations for q matrices, help Sean reverse the rows and columns of each matrix in the
# best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.

# Example
# matrix = [[1,2] [3,4]]
# 1 2
# 3 4

# It is 2 x 2 and we want to maximize the top left quadrant, a 1 x 1 matrix. Reverse row :
# 1 2
# 4 3

# And now reverse column 0:
# 4 2
# 1 3

# The maximal sum is 4.

# Function Description

# Complete the flippingMatrix function in the editor below.
# flippingMatrix has the following parameters:
# - int matrix[2n][2n]: a 2-dimensional array of integers

# Returns
# - int: the maximum sum possible.

# Input Format
# The first line contains an integer q, the number of queries.

# The next sets of lines are in the following format:
# The first line of each query contains an integer, n.
# Each of the next 2n lines contains 2n space-separated integers matrix[i][j] in row i of the matrix.

# Sample Input
# STDIN Function
# ----- --------
# 1 q = 1
# 2 n = 2
# 112 42 83 119 matrix = [[112, 42, 83, 119], [56, 125, 56, 49], \
# 56 125 56 49 [15, 78, 101, 43], [62, 98, 114, 108]]
# 15 78 101 43
# 62 98 114 108

# Sample Output
# 414

# Explanation
# The sum of values in the n x n submatrix in the upper-left quadrant is 119 + 114 + 56 + 125 = 414.

def flippingMatrix(n, matrix):
    sum = 0
    for i in range(0,n):
        for j in range(0,n):
            n1 = matrix[i][j]
            n2 = matrix[i][len(matrix)-1-j]
            n3 = matrix[len(matrix)-1-i][j]
            n4 = matrix[len(matrix)-1-i][len(matrix)-1-j]
            sum += max(n1, n2, n3, n4)
            
    return sum

matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]

result = flippingMatrix(2, matrix)

print(result)

# Sample input
# 1
# 2
# 112 42 83 119
# 56 125 56 49
# 15 78 101 43
# 62 98 114 108