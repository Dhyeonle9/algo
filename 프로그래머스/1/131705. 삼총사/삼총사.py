from itertools import combinations
def solution(number):
    answer = 0
    combi = list(combinations(number, 3))
    for com in combi:
        if sum(com) == 0:
            answer += 1
    return answer