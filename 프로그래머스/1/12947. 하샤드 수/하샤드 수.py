def solution(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    if x % sum:
        return False
    else:
        return True