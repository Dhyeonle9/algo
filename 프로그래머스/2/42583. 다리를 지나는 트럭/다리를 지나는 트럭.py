# 큐
def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    time = 0
    sum_weights = 0
    temp = 0
    while truck_weights:
        time += 1
        sum_weights -= bridge.pop()
        if sum_weights + truck_weights[0] <= weight:
            temp = truck_weights.pop(0)
            bridge.insert(0, temp)
            sum_weights += temp
        else:
            bridge.insert(0, 0)
    time += bridge_length
    return time