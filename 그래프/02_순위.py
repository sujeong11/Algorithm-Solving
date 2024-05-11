def solution(n, results):
    answer = 0
    graph = [[None] * n for _ in range(n)]
    
    for win, lose in results:
        graph[win - 1][lose - 1] = True
        graph[lose - 1][win - 1] = False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[j][i] == None:
                    continue
                    
                # 플로이드 워셜: j점에서 k점을 갈 때 i점을 거쳐 j -> i -> k로 갈 수 있는가
                if graph[j][i] == graph[i][k]:
                    graph[j][k] = graph[j][i]
                    graph[k][j] = not graph[j][i]
                    
    for i in range(n):
        # 자기 자신은 제외
        if None not in graph[i][:i] + graph[i][i+1:]:
            answer += 1
            
    return answer
