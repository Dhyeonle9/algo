def solution(array):
    arr = [0] * (max(array)+1)

    for i in array:
        if i in array:
            arr[i] += 1
        else:
            arr[i] = 1
    c = 0

    for j in arr:
        if j == max(arr):
            c += 1
    if c > 1:
        return -1
    else:
        return arr.index(max(arr))
    return answer