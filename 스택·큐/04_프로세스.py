# 답안 참고해 풀었음

def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    
    while True:
        cur = queue.pop(0)
        # queue 안에 자신(맨 앞 원소)보다 우선순위가 높은 원소 있다면 맨 뒤에 다시 넣음
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
