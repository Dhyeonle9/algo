def solution(a, b, n):
    answer = 0
    temp = 0
    while n >= a:
        answer += (n//a) * b
        temp = n % a
        n = (n//a) * b + temp

    return answer 