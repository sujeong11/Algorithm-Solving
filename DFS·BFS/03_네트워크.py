def solution(n, computers):
    answer = 0
    visited = [False] * n
  
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i, visited)
            answer += 1
          
    return answer

def dfs(n, computers, start, visited):
    visited[start] = True

    for i in range(n):
        if start != i and computers[start][i] == 1:
            if not visited[i]: # 대칭이므로 방문 여부 체크
                dfs(n, computers, i, visited)
