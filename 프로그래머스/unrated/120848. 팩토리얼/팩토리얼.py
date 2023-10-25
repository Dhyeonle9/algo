def solution(n):
    fact = 1
    answer = 1
    while fact <= n:        
        answer += 1
        fact *= answer
    return answer - 1
    