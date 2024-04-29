# 풀이 참고
def solution(distance, rocks, n):
    answer = 0
    left, right = 1, distance
    rocks.sort()
    rocks.append(distance)
    
    while left <= right:
        mid = (left + right) // 2 # 각 지점 사이 거리의 최소값
        prev_rock = 0 # 왼쪽에 위치한 바위
        remove_count = 0 # 제거한 바위 개수
        
        for rock in rocks:
            dist = rock - prev_rock # 돌 사이 거리
            
            if dist < mid:
                remove_count += 1
            else:
                prev_rock = rock

            if remove_count > n:
                break
                
        if remove_count > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    
    return answer
