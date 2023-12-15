# def solution(numbers):
#     answer = ''
#     numbers = list(map(str, numbers))
#     len_num = len(''.join(numbers))
#     max_= '0'
#     while len(answer)<len_num:          
#         for num in numbers:
#             if int(num[0])>int(max_[0]) or (int(num[0])==int(max_[0]) and num+max_ > max_+num):
#                 max_ = num           
#         answer += max_
#         del numbers[numbers.index(max_)]
#         max_= '0'
#     if answer[0]=='0':
#         return "0"
#     return answer

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
import functools
def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
