# [BFS]: numbers의 숫자를 더하거나 뺀 경우를 수평적으로 추가 후 비교
def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for num in numbers:
        tmp = []

        # 이전의 결과들을 꺼내 추가 계산 후 갱신
        for leaf in leaves:
            tmp.append(leaf + num)
            tmp.append(leaf - num)          
        leaves = tmp
        
    for leaf in leaves:
        if leaf == target:
            answer += 1
            
    return answer

# [DFS]: 가능한 모든 연산을 하나씩 계산해 비교
# count = 0
#  
# def dfs(numbers, target, current, idx):
#     global count
#   
#     연산을 완료했다면 값 비교 
#     if idx == len(numbers):
#         if current == target:
#             cnt += 1
#         return# 같지 않다면 그냥 리턴
#  
#     dfs(numbers, target, current + numbers[idx], idx + 1)
#     dfs(numbers, target, current - numbers[idx], idx + 1)
#  
# def solution(numbers, target):
#     dfs(numbers, target, 0, 0)
#     return count
