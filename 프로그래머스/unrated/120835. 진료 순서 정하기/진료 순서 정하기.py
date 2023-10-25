def solution(emergency):
    answer = [0] * len(emergency)
    for i in range(len(emergency)):
        answer[emergency.index(max(emergency))] = i+1
        emergency[emergency.index(max(emergency))] = 0
    return answer