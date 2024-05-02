# 풀이 참고
def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    for (y, x) in puddles: # 잠긴 곳 표시
        dp[x][y] = -1
        
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if dp[x][y] != -1:
                if x > 1 and dp[x - 1][y] != -1: # 위쪽에서 오는 경우
                    dp[x][y] += dp[x - 1][y]
                if y > 1 and dp[x][y - 1] != -1: # 왼쪽에서 오는 경우
                    dp[x][y] += dp[x][y - 1]
                
    return dp[n][m] % 1000000007
