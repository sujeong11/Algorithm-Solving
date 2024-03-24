def solution(arr):
    answer = []
    for i in range(len(arr) - 1):
        if (arr[i] != arr[i + 1]):
            answer.append(arr[i])
    answer.append(arr[-1])
    return answer

# 다른 사람 풀이 1
# def solution(arr):
#     answer = []
#     for i in range(len(arr)):
#         if [arr[i]] != arr[i + 1: i + 2]:
#             answer.append(arr[i])
#     return answer
