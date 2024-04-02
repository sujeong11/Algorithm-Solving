def solution(array, commands):
    answer = []
  
    for cmd in commands:
        sort_arr = sorted(array[cmd[0] - 1:cmd[1]])
        answer.append(sort_arr[cmd[2] - 1])
      
    return answer
