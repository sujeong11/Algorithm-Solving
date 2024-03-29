from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        price = prices.popleft()
        second = 0
        
        for p in prices:
            second += 1
            if (price > p):
                break
        
        answer.append(second)
        
    return answer
