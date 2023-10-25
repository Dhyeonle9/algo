def solution(common):
    cd = common[1] - common[0]
    if common[0] != 0:
        cr = common[1] // common[0]
    
    if cd == common[2] - common[1]:
        return common[-1] + cd
    elif cr == common[2] // common[1]:
        return common[-1] * cr
    