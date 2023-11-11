def solution(s):
    p = 'pP'
    y = 'yY'
    for i in s:
        if i in p:
            s = s.replace(i,'1')
        elif i in y:
            s = s.replace(i,'2')
    if s.count('1') == s.count('2'):
        return True
    else:
        return False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
