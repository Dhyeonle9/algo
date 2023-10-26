# def solution(strlist):
#     answer = []
#     for i in strlist:
#         answer.append(len(i))
#     return answer

def solution(strlist):
    return list(map(len, strlist))