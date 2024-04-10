from collections import deque

def solution(begin, target, words):
    if target not in words:
        return  0
    return bfs(begin, target, words)

def bfs(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    
    while queue:
        cur_word, step = queue.popleft()
        
        if cur_word == target:
            return step
        
        for word in words:
            count = 0
            # 단어 길이만큼 반복하며 같지 않은 알파벳 개수 확인
            for i in range(len(cur_word)):
                if cur_word[i] != word[i]:
                    count += 1
                    
            if count == 1: 
                queue.append([word, step + 1])
