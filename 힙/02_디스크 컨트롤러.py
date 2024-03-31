import heapq

def solution(jobs):
    answer, current_time, count, start = 0, 0, 0, -1
    heap = []

    while count < len(jobs):
        # 현재 시간에서 처리할 수 있는 디스크 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= current_time:
                heapq.heappush(heap, [j[1], j[0]])

        if len(heap) > 0:
            disk = heapq.heappop(heap)
            start = current_time
            current_time += disk[0]
            answer += (current_time - disk[1])
            count += 1
        else:
            current_time += 1 # 처리할 작업이 없는 경우 시간에 +1만

    return answer // len(jobs)
