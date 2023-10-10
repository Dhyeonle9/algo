# def solution(num_list):

#     num_list.reverse()
#     answer = num_list
#     return answer

# def solution(num_list):
#     answer = []

#     for i in range(len(num_list)):
#         # num_list[i]
#         # print(i)
#         # print(len(num_list)-i-1) # 전체길이 - i: 뒤에서부터 나옴
#         answer.append(num_list[len(num_list)-i-1])
#     return answer


# def solution(num_list):
#     answer = []
#     for num in range(len(num_list)-1, 0, -1):
#         answer.append(num)
#     return answer

def solution(num_list):
    answer = []
    for num in num_list:
        answer.insert(0, num)

    return answer
    
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))