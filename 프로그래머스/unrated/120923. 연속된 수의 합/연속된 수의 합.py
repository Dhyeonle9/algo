# def solution(num, total):
#     if num % 2:
#         return list(range(total//num-num//2, total//num-num//2+num))
#     else:
#         return list(range(total//num-num//2+1, total//num-num//2+num+1))
    
def solution(num, total):
    answer = []
    num_list = list(range(-50, 500))
    for i in range(len(num_list)):
        if sum(num_list[i:i+num]) == total:
            answer = num_list[i:i+num]
            break
    return answer