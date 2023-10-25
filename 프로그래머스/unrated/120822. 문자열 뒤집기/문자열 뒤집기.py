def solution(my_string):
    answer = ''
    for char in my_string[::-1]:
        answer += char
    return answer