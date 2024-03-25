import math

def solution(progresses, speeds):
    answer = []
    work_date = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    index = 0

    for i in range(len(work_date)):
        if work_date[i] > work_date[index]:
            answer.append(i - index)
            index = i

    answer.append(len(work_date) - index)
    
    return answer
