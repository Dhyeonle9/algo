def solution(x, n):
    answer=[]
    if x!= 0:
        for i in range(x, x*(1+n), x):
            answer.append(i)
    else:
        answer = [0 for i in range(n)]
    return answer