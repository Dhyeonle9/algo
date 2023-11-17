
def solution(score):
    scr = []
    answer = []
    sorted_scr = []
    for i in score:
        scr.append(sum(i))
    sorted_scr = sorted(scr, reverse=True)
    for j in scr:
        answer.append(sorted_scr.index(j)+1)
    return answer