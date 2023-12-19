def solution(participant, completion):
    h_dic = {}
    h_sum = 0
    for part in participant:
        h_dic[hash(part)] = part
        h_sum += hash(part)
        
    for comp in completion:
        h_sum -= hash(comp)
    return h_dic[h_sum]