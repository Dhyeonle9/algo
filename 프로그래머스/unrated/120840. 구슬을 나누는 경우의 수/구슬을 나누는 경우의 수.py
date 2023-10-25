def solution(balls, share):
    u, d = 1, 1

    for i in range(balls, balls - share, -1):
        u *= i
        d *= (balls -i + 1)
    return u/d