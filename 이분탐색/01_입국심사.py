def solution(n, times):
    answer = 0
    start, end = 1, max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        count = 0 # 심사한 사람의 수
        
        for time in times:
            count += (mid // time)
            if count >= n:
                break
        
        if count >= n: # 심사한 사람의 수가 심사 받아야할 사람의 수보다 많거나 같을 경우
            answer = mid
            end = mid - 1
        elif count < n: # 심사한 사람의 수가 심사 받아야할 사람보다 적음 -> 시간이 더 필요
            start = mid + 1
    
    return answer
