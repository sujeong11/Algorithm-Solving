# 답안 일부를 참고해 풀었음
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur_weight = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    while len(truck_weights) > 0:
        cur_weight -= bridge.popleft() # 다리에서 나간 트럭(맨 앞)의 무게 제거
        answer += 1
        
        if cur_weight + truck_weights[0] <= weight:
            cur_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else: 
            bridge.append(0)
    
    answer += bridge_length # 마지막 트럭이 지나간 길이
    
    return answer
