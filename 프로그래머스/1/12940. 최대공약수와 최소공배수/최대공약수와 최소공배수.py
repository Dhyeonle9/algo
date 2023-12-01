def solution(n, m):
    answer = []
    if max(n, m) % min(n, m) == 0:
        return [min(n, m), max(n, m)]
    else:
        for i in range(min(n, m), 0, -1):
            if n % i == 0 and m % i == 0:
                return [i, (n*m/i)]
