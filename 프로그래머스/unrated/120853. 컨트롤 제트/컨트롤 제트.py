def solution(s):
    answer = []
    for i in list(s.split()):
        if i == 'Z':
            answer.pop()
        else:
            answer.append(int(i))
    return sum(answer)