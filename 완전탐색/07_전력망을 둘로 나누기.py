# 풀이 참고
def dfs(v, graph, visited, connect_wires):
    count = 1
    visited[v] = True
    
    for i in graph[v]: # 방문한 적이 없고, 임의로 없앤 간선이 아니라면 카운트 증가
        if visited[i] == False and connect_wires[v][i]:
            count += dfs(i, graph, visited, connect_wires)
        
    return count

def solution(n, wires):
    answer = 1e9
    connect_wires = [[True] * (n + 1) for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
        
    for x, y in wires:
        visited = [False] * (n + 1)
        connect_wires[x][y] = False # 간선 끊기
      
        count_x = dfs(x, graph, visited, connect_wires)
        count_y = dfs(y, graph, visited, connect_wires)
        connect_wires[x][y] = True # 간선 다시 연결
        answer = min(answer, abs(count_x - count_y))
        
    return answer
