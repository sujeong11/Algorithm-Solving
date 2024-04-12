def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    result = []
    
    for idx, answer in enumerate(answers):
    	if person1[idx%len(person1)] == answer:
          scores[0] += 1
    	if person2[idx%len(person2)] == answer:
          scores[1] += 1
    	if person3[idx%len(person3)] == answer:
          scores[2] += 1   
            
    for idx, score in enumerate(scores):
    	if score == max(scores):
          result.append(idx + 1)
            
    return result
