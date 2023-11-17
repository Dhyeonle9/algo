def solution(s):
    answer = []
    cnt = 0
    z = 0
    while s != '1':
        z += s.count('0')
        s = bin(len(s.replace('0','')))[2:]
        cnt += 1
    answer = [cnt,z]
    return answer