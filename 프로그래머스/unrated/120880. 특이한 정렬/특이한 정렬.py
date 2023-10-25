# 1차시도
# def solution(numlist, n):
#     answer = []
#     num = [[value, abs(value-n)] for i, value in enumerate(numlist)]
#     num.sort(key=lambda x: (x[1], -x[0]))
#     for i in range(len(num)):
#         answer.append(num[i][0])
#     return answer

# 2차시도
def solution(numlist, n):
    answer = []
    numlist.sort(key = lambda x: (abs(x-n), -x)) 
    for i in numlist:
        answer.append(i)
    return answer