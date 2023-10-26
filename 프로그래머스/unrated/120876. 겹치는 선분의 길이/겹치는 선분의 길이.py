def solution(lines):
    arr = [0 for _ in range(-100, 101)]
    answer = []
    for i in lines:
        for j in range(i[0], i[1]):
            arr[j] += 1
    
    answer = arr.count(2) + arr.count(3)
    return answer

# 확인해보기
# def solution(lines):
#     sets = [set(range(min(l), max(l))) for l in lines]
#     return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])