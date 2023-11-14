def solution(s):
    s = s.lower().split(" ")
    for i, x in enumerate(s):
        if x != "" and x[0].isalpha():
            s[i] = x.capitalize()
    return ' '.join(s)         