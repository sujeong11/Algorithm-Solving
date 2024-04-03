def solution(n, lost, reserve): 
    distinct_lost = set(lost) - set(reserve) 
    distinct_reserve = set(reserve) - set(lost) 
    
    for r in distinct_reserve: 
        front, back = r - 1, r + 1
      
        if front in distinct_lost: 
            distinct_lost.remove(front)   
        elif back in distinct_lost: 
            distinct_lost.remove(back)
            
    return  n - len(distinct_lost)
