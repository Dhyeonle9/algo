def solution(n):
    answer = [0]
    i = 1
    while len(answer) < n+1:
        if '3' not in str(i) and i % 3:
            answer.append(i)
        i += 1
            
    return answer[n]