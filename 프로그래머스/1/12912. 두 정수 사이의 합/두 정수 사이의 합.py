def solution(a, b):
    answer = 0
    a, b = sorted([a, b])
    for i in range(a, b+1):
        answer += i   
    return answer