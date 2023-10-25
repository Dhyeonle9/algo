def solution(my_string): 
    cal = list(my_string.split())
    answer = int(cal[0])
    for i in range(len(cal)):
        if cal[i] == '+':
            answer += int(cal[i+1])
        elif cal[i] == '-':
            answer -= int(cal[i+1])
    return answer