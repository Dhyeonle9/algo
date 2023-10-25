def solution(n):
    answer = 0
    for i in range(n, 0, -1):
        check = 0
        for j in range(int(i ** 0.5), 0, -1):
            if i % j == 0:
                check += 2
        if check > 2:
            answer += 1

    return answer