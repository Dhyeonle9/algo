def solution(left, right):
    result = 0
    for i in range(left, right+1):
        divisor = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                if i == j ** 2:
                    divisor += 1
                else:
                    divisor += 2
        if divisor % 2:
            result -= i
        else:
            result += i
    return result