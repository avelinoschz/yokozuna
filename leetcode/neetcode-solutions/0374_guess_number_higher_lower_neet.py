# 374. Guess Number Higher or Lower

# neetcode video solution
# https://www.youtube.com/watch?v=xW4QsTtaCa4

# Time complexity: O(log n)
# Space complexity: O(1)
def guessNumber(n: int) -> int:
    l, r = 1, n
    # while True: # this applies only here, because leetcode guarantees having a solution
    while l <= r:
        m = (l + r) // 2
        res = guess(m)
        if res > 0: # 1
            l = m + 1
        elif res < 0: # -1
            r = m - 1
        else:
            return m
    
    return -1 # in the context of leetcode this doesn't apply, because it guarantees a solution
       
def guess(num: int) -> int:
    pick = 6
    if pick > num:
        return 1
    elif pick < num:
        return -1
    else:
        return 0
    
result = guessNumber(6)
print(result)
