def solution(n):
    gcd = 0
    for i in  range(min(6, n), 0, -1):
        if 6 % i == 0 and n % i == 0:
            gcd = i
            break
        

    return n / gcd