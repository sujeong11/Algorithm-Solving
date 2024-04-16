from itertools import permutations

def solution(k, dungeons):
    answer = -1
    dungeons = list(permutations(dungeons, len(dungeons)))
    
    for dungeon in dungeons:
        _k = k
        count = 0
        
        for d in dungeon:
            if (d[0] <= _k):
                _k -= d[1]
                count += 1
                
        answer = max(count, answer)

    return answer
