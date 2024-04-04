# 풀이를 참고해서 품

def solution(name):
    answer = 0
    min_move = len(name) - 1 # 기본 좌우이동 횟수
    
    for i, char in enumerate(name):
        # 'A에서 출발한 값'과 'Z로 이동 후(+1) 출발한 값' 중 최솟값
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        next = i + 1
        
        # 연속된 A를 찾는 부분
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # '기존의 min_move 값', '연속된 A 왼쪽 시작', '연속된 A의 오른쪽 시작' 중 최솟값
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])
        
    # 조이스틱 조작 횟수: 알파벳 변경 횟수 + 좌우이동 횟수
    return answer + min_move
