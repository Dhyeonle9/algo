def solution(participant, completion):
    h_dic = {}
    h_sum = 0
    for part in participant:
        h_dic[hash(part)] = part
        h_sum += hash(part)
        
    for comp in completion:
        h_sum -= hash(comp)
    return h_dic[h_sum]

# 시간초과
# def solution(participant, completion):        
#     for comp in completion:
#         participant.remove(comp)
#     return participant[0]

# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
    
#     for part, comp in zip(participant, completion):
#         if part != comp:
#             return part
#     return participant[-1]

# from collections import Counter

# def solution(participant, completion):
#     answer = ''
#     dict_result=Counter(participant)-Counter(completion)
#     return list(dict_result.keys())[0]   