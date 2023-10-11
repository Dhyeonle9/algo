def solution(my_string):
    answer = 0
    for char in my_string:
        if char.isdigit():
            answer += int(char)

    return answer

# def solution(my_string):
#     answer = 0
#     for char in my_string:
#         try:
#             answer += int(char)
#         except:
#             continue

#     return answer

def solution(my_string):
    answer = 0

    for char in my_string:
        if not (ord('A') <= ord(char) <= ord('z')):
            answer += int(char)


    # for char in my_string:
    #     if ord('0') <= ord(char) <= ord('9'):
    #         answer += int(char)

    
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))