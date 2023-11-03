# def solution(spell, dic):
#     answer = 0
#     for i in dic:
#         if len(spell) == len(i):
#             for j in spell:
#                 if j in i:
#                     continue
#                 else:
#                     answer = 2
#                     break
#             else:
#                 answer = 1
#                 break
#         else:
#             answer = 2
#             continue               
#     return answer

def solution(spell, dic):
    for i in dic:
        count_num = 0
        for j in spell:
            if i.count(j) == 1:
                count_num += 1
                print(count_num)
        if count_num != len(spell):
            continue
        elif count_num == len(spell):
            return 1
        

    return 2