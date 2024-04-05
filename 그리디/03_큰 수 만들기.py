# 풀이 참고해서 품

def solution(number, k):
    answer = []

    for n in number:
        # 현재 숫자보다 작은 값이 있다면 끝에서부터 제거
        while k > 0 and answer and answer[-1] < n:
            answer.pop()
            k -= 1
        answer.append(n)

    return ''.join(answer[:len(answer) - k])
