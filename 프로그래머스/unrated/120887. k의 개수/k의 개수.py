def solution(i, j, k):
    answer = ''.join(map(str,list(range(i, j+1))))
    return answer.count(str(k))