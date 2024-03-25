# 682. Baseball Number

# https://leetcode.com/problems/baseball-game/

# You are keeping the scores for a baseball game with strange rules. 
# At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] 
# is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate 
# calculations fit in a 32-bit integer and that all operations are valid.

# Example 1:

# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.

# Original answer
# def calPoints(operations):
#     """
#     :type operations: List[str]
#     :rtype: int
#     """
#     score = []
#     for op in operations:
#         if op == '+':
#             size = len(score)
#             score_last = score[size-1]
#             score_prev_to_last = score[size-2]
#             score.append(int(score_prev_to_last) + int(score_last))
#         elif op == 'D':
#             size = len(score)
#             score_last = score[size-1]
#             score.append(int(score_last) * 2)
#         elif op == 'C':
#             score.pop()
#         else:
#             score.append(int(op))

#     sum = 0
#     for num in score:
#         sum += int(num)

#     return sum


# More pythonic way
def calPoints(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    score = []
    for op in operations:
        if op == '+':
            score.append(score[-1] + score[-2])
        elif op == 'D':
            score.append(score[-1] * 2)
        elif op == 'C':
            score.pop()
        else:
            score.append(int(op))

    return sum(score)

# Input: ops = ["5","-2","4","C","D","9","+","+"]
# Output: 27

ops = ["5","-2","4","C","D","9","+","+"]
result = calPoints(ops)
print(result)
