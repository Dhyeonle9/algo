def solution(spell, dic):
    answer = 0
    check = 0
    for i in dic:
        if len(spell) == len(i):
            for j in spell:
                if j in i:
                    continue
                else:
                    answer = 2
                    break
            else:
                answer = 1
                break
        else:
            answer = 2
            continue
                
    return answer