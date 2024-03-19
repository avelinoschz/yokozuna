# https://www.hackerrank.com/interview/preparation-kits/three-month-preparation-kit/three-month-week-one/challenges

# Given five positive integers, find the minimum and maximum values that can be 
# calculated by summing exactly four of the five integers. Then print the respective 
# minimum and maximum values as a single line of two space-separated long integers.

# Example
# arr = [1,3,5,7,9]
# The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24. 
# The function prints
# 16 24

# This is a super short an easy python way
# but this is not efficient, because of the sorting
# def miniMaxSum(arr):    
#     arr.sort()
    
#     min_sum = sum(arr[:-1]) 
#     max_sum = sum(arr[1:])
    
#     print(min_sum, max_sum)

def miniMaxSum(arr):
    min = arr[0]
    max = arr[0]
    sum = 0
    
    for i in arr:
        if i < min:
            min = i

        if i > max:
            max = i

        sum += i

    min_sum = sum - max
    max_sum = sum - min

    print(min_sum, max_sum)


arr = [1,3,5,7,9]
miniMaxSum(arr)