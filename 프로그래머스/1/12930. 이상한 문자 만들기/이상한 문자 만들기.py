def solution(s):
    answer = []
    s = list(s.split(" "))
    for word in s:
        w = ''
        for i in range(len(word)):
            if i % 2:
                w += word[i].lower()
            else:
                w += word[i].upper()
        answer.append(w)

    return ' '.join(answer)