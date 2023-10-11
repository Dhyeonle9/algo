# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 1,000
# my_string은 소문자, 대문자 그리고 한자리 자연수로만 구성되어있습니다.

# 입출력 예
# my_string	        result
# "aAb1B2cC34oOp"	10
# "1a2b3c4d123"	    16

# def solution(my_string):
#     answer = 0
#     num = list(map(str, list(range(1,10))))
#     for char in my_string:
#         if char in num:
#             answer += int(char)

#     return answer


def solution(my_string):
    answer = 0
    for char in my_string:
        try:
            answer += int(char)
        except:
            pass

    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))