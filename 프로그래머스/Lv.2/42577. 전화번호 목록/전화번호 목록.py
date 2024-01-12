# # 시간초과
# def solution(phone_book):
#     answer = True
#     for i in range(len(phone_book)-1):
#         for j in range(i+1,len(phone_book)):
#             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                 return False        
#     return True

# 해시 사용
def solution(phone_book):
    hash_map = {}
    # 해시에 번호 넣기
    for phone in phone_book:
        hash_map[phone] = 1
    # 찾기
    for phone in phone_book:
        num = ""
        for number in phone:
            num += number
            if num in hash_map and num != phone:
                return False
    return True
# def solution(phone_book):
#     hash_map = {}
#     # 해시에 번호 넣기
#     for phone in phone_book:
#         hash_map[phone] = 1
#     # 찾기
#     for phone in phone_book:
#         for ha in hash_map.keys():
#             if phone != ha and phone == ha[:len(phone)]:
#                 return False
#     return True


# 다른코드
# def solution(phone_book):
#     phone_book.sort()
#     for i in range(len(phone_book) - 1):
#         if phone_book[i] in phone_book[i + 1][0:len(phone_book[i])]:
#             return False
#     return True

# 다른코드 2
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True