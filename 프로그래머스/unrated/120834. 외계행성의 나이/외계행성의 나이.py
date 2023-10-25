def solution(age):
    ag = 'abcdefghij'
    answer = ''
    for i in str(age):    
        answer += ag[int(i)]
    return answer