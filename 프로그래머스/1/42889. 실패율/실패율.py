def solution(N, stages):
    answer = {}
    for i in range(1, N+1):
        t = [t for t in stages if t>=i]
        if len(t) == 0:
            answer[i] = 0
        else:
            answer[i] = stages.count(i)/len(t)
    return sorted(answer, key=lambda x : answer[x], reverse=True)