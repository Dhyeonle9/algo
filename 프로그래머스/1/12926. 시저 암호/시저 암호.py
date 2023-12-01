
# def solution(s, n):
    # answer = ''
    # c = ''
    # for i in s:
    #     if i == ' ':
    #         answer += ' '
    #     else:
    #         c = chr(ord(i) + n)
    #         if not c.isalpha or c.islower() != i.islower():
    #             c = chr(ord(c) -26)
    #         answer += c
    # return answer
    
# 아스키코드 활용
# 대문자 65 ~ 90(26)
# 91~96 기호
# 소문자 97 ~ 122(26)
# 123~126 기호
def solution(s, n):
    answer = ''
    for i in s:
        # 문자열이 공백일 경우 공백 추가
        if i == ' ':
            answer += i
            continue
            
        if i.isupper() and ord(i) + n > ord('Z'):
            answer += chr(ord(i) + n - 26) 

        elif i.islower() and ord(i) + n > ord('z'):
            answer += chr(ord(i) + n - 26)  
        else:
            answer += chr(ord(i) + n)           
    return answer