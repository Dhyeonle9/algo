# def solution(n):
#     answer = 0
#     for num in str(n):
#         answer += int(num)
#     return answer

# 한줄코드
def solution(n):
    return sum(list(map(int,str(n))))