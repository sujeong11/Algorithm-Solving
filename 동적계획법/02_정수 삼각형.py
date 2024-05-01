# 풀이 참고
# 줄을 증가시키면서 이전 줄에서 계산한 결과를 더해 마지막 줄의 가장 큰 값이 정답
def solution(triangle):
    dp = triangle
    
    for i in range(1, len(triangle)): # 줄
        for j in range(i + 1): # 해당 줄의 인덱스
            if j == 0: # 가장 왼쪽인 경우
                dp[i][j] += dp[i - 1][j]
            elif j == i: # 가장 오른쪽인 경우
                dp[i][j] += dp[i - 1][j - 1]
            else: # 가운데인 경우
                dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1])
                
    return max(dp[-1])
