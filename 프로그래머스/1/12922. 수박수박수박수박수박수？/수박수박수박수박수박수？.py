def solution(n):
    answer = ''
    wm = '수박'
    for i in range(n):
        answer += wm[i%2]
    return answer