def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] in s[:i]:
            answer.append(s[:i][::-1].index(s[i])+1)
        else:
            answer.append(-1)      
    return answer