# 답안 참고해서 품
def solution(numbers):
    str_numbers = list(map(str, numbers)) # 문자열로 바꾸는 이유: 숫자와 문자열은 대소비교 기준이 다르기 때문
    str_numbers.sort(key=lambda num: num * 3, reverse=True) # 입력 값은 1000 이하로 3자리 숫자를 만들어 비교

    # int 타입으로 바꾸는 이유: '00'을 '0'으로 바꿔주기 위함
    return str(int(''.join(str_numbers)))
