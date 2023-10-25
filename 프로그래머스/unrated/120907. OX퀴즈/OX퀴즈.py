def solution(quiz):
    answer = []
    for cal in quiz:
        factor = cal.split(' ')
        if factor[1] == '+':
            if (int(factor[0]) + int(factor[2]) == int(factor[4])):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if (int(factor[0]) - int(factor[2]) == int(factor[4])):
                answer.append("O")
            else:
                answer.append("X")
    return answer