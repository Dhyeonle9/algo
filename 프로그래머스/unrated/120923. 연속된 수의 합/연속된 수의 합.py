def solution(num, total):
    if num % 2:
        return list(range(total//num-num//2, total//num-num//2+num))
    else:
        return list(range(total//num-num//2+1, total//num-num//2+num+1))