def solution(babbling):
    babb = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    for i in range(len(babbling)):
        for j in babb:
            babbling[i] = babbling[i].replace(j, '1')
    for i in babbling:
        if i.isdigit():
            answer+=1
    return answer