def solution(numbers, direction):
    answer = []
    temp = ''
    if direction == 'left':
        temp = [numbers.pop(0)]
        answer = numbers + temp
        return answer
    else:
        answer.append(numbers.pop())
        answer += numbers
        return answer