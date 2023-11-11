def solution(s):
    # p = 'pP'
    # y = 'yY'
    # for i in s:
    #     if i in p:
    #         s = s.replace(i,'1')
    #     elif i in y:
    #         s = s.replace(i,'2')
    # if s.count('1') == s.count('2'):
    #     return True
    # else:
    #     return False
    if s.lower().count('p')==s.lower().count('y'):
        return True
    else:
        return False