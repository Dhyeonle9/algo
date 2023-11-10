def solution(numbers, direction):
    temp = []
    if direction == 'left':
        temp.append(numbers.pop(0))
        return numbers + temp
    else:
        temp.append(numbers.pop())
        return temp + numbers