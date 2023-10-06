# 문제 설명
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ numbers의 원소 ≤ 1,000
# 1 ≤ numbers의 길이 ≤ 100
# 정답의 소수 부분이 .0 또는 .5인 경우만 입력으로 주어집니다.

def solution(numbers):
    if 1<= len(numbers) <= 100:
        if 1<= min(numbers) and max(numbers)<= 1000:    
            answer = sum(numbers) / len(numbers)
    return answer

# 함수 쓰지않기
# def solution(numbers):
#     answer = 0
#     n = 0
#     for i in numbers:
#         answer += i
#         n += 1
#     answer /= n
#     return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))
