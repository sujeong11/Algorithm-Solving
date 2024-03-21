def solution(phone_book):    
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if (phone_book[i+1].startswith(phone_book[i])):
            return False
    return True	

# 해시를 사용한 답안
# def solution(phoneBook):
#     hashMap = {}
#    
#     for phoneNumer in phoneBook:
#         hashMap[phoneNumer] = 1
#
#     for phoneNumer in phoneBook:
#         result = ""
#         for num in phoneNumer:
#             result += num
#             if result in hashMap and result != phoneNumer:
#                 return False
#     return True

# 기타 답안
# def solution(phoneBook):
#     phoneBook.sort()
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True
