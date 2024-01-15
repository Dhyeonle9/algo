def solution(n):
    answer = 0
    for num in range(1, int(n ** 0.5)+1):
        if  n % num ==0:
            answer += 2
        if num ** 2 == n:
            answer -= 1

    return answer

# 한줄코드
# def solution(array, height):
#     return sum(1 for a in array if a > height)