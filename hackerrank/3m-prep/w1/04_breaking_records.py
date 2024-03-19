# Maria plays college basketball and wants to go pro. Each season she maintains a 
# record of her play. She tabulates the number of times she breaks her season 
# record for most points and least points in a game. Points scored in the first 
# game establish her record for the season, and she begins counting from there.

# Example
# Scores are in the same order as the games played. She tabulates her results as follows:
#                                     Count
#    Game  Score  Minimum  Maximum   Min Max
#     0      12     12       12       0   0
#     1      24     12       24       0   1
#     2      10     10       24       1   1
#     3      24     10       24       1   1
# Given the scores for a season, determine the number of times Maria breaks her records 
# for most and least points scored during the season.

def breakingRecords(scores):
    min = 0
    max = 0
    min_score = scores[0]
    max_score = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
            max += 1
        elif scores[i] < min_score:
            min_score = scores[i]
            min += 1
        
    return [max, min]

scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
result = breakingRecords(scores)
print(result)
