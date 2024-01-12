def solution(clothes):
    answer = 1
    clo_dic = {}
    for clo in clothes:
        if clo[1] in clo_dic:
            clo_dic[clo[1]] += 1
        else:
            clo_dic[clo[1]] = 1
# 경우의 수 ()
    for num in clo_dic.values():
        answer *= (num+1)
    return answer-1