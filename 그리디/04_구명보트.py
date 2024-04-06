# 답안을 참고해서 품

def solution(people, limit):
    answer, start_idx, end_idx = 0, 0, len(people) - 1
    people.sort()

    while start_idx < end_idx:
        if people[end_idx] + people[start_idx] <= limit:
            start_idx += 1
            answer += 1
        end_idx -= 1
        
    return len(people) - answer
