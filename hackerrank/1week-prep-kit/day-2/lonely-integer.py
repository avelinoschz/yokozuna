# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example
# a = [1, 2, 3, 4, 3, 2, 1]

# The unique element is 4.

# Function Description
# Complete the lonelyinteger function in the editor below.
# lonelyinteger has the following parameter(s):
# int a[n]: an array of integers

# Returns
# int: the element that occurs only once

# Input Format
# The first line contains a single integer, , the number of integers in the array.
# The second line contains  space-separated integers that describe the values in a.

def lonelyinteger(a):
    if len(a) == 1:
        return a[0]
        
    tracker = {}        
    for n in a:
        if n not in tracker:
            tracker[n] = 1
            continue
        tracker[n] +=1 
    
    for k,v in tracker.items():
        if v == 1:
            return k

def lonelyinteger2(arr):
    if len(arr) == 1:
        return arr[0]
        
    arr.sort()

    curr = arr[0]
    counter = 0
    for n in arr:
        if n == curr:
            counter += 1
        else:
            if counter == 1:
                return curr
            
            counter = 1
            curr = n

    if counter == 1:
        return curr



result = lonelyinteger2([0, 0, 1, 2, 1])
print(f"input: [0, 0, 1, 2, 1] | output: {result}")