# 1929. Concatenation of Array

# neetcode video solution
# https://www.youtube.com/watch?v=68isPRHgcFQ

# Time complexity: O(n + 2) which is O(n)
# Space complexity: O(n)

# Another way to do it could be not using the extra list
# Just appending to the original array while traversing
# and that could be space complexity O(1)

ans = []
nums = [2,1,3]

for i in range(2):
    for n in nums:
        ans.append(n)

print(ans)