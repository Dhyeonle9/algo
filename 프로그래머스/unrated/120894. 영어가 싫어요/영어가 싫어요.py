def solution(numbers):
    answer = ""
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in num:
        numbers = numbers.replace(i,str(num.index(i)))
    return int(numbers)