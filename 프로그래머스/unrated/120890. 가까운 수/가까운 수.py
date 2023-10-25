def solution(array, n):
    array.append(n)
    array.sort()
    if 0 < array.index(n) < len(array)-1:
        if abs(n - array[array.index(n)-1]) > abs(n - array[array.index(n)+1]):
            return array[array.index(n)+1]
        else: 
            return array[array.index(n)-1]
    elif 0 == array.index(n):
        return array[1]
    else:
        return array[-2]
        