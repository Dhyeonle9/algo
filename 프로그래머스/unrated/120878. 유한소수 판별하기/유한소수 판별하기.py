def solution(a, b):
    for i in range(min(a,b), 1, -1):
        if a % i == 0 and b % i == 0:
            a /= i
            b /= i
    while b % 2 == 0 or b % 5 == 0:
        if b % 2 == 0:
            b /= 2
        elif b % 5 == 0:
            b /= 5
               
    return 1 if b == 1 else 2