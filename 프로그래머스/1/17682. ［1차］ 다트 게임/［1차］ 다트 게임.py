import re

def solution(dartResult):
    answer = []
    power = {'S': 1, 'D': 2, 'T': 3}
    a = re.findall('\d+[S, D, T][*, #]?', dartResult)
    for i in a:
        if '#' in i or '*' in i:
            answer.append(int(i[:-2]) ** power[i[-2]])
            if i[-1] == '#':
                answer[-1] = answer[-1] * (-1)
            elif i[-1] == '*' and len(answer) >= 2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
                
        else:
            answer.append(int(i[:-1]) ** power[i[-1]])
    return sum(answer)