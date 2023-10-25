def solution(n):
    num = 2
    answer = set()
    while num <= n:
        if n % num == 0:
            answer.add(num)
            n /= num
        else:
            num += 1   
    return sorted(list(answer))