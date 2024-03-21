from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

# 해시를 사용한 답안
# def solution(participant, completion):
#     hashDict = {}
#     hashSum = 0
# 
#     for p in participant:
#         hashDict[hash(p)] = p
#         hashSum += hash(p)
# 
#     for c in completion:
#         hashSum -= hash(c)
# 
#     return hashDict[hashSum]
