def solution(nums):
    num = len(nums)/2
    pos_num = len(set(nums))
    if num >= pos_num:
        return pos_num
    else: 
        return num
