def solution(dots):
    width = []
    length = []
    for x, y in dots:
        width.append(x)
        length.append(y)
    return  (max(width) - min(width)) * (max(length) - min(length))