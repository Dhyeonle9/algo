# 문제 설명
# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

# 제한사항
# 0 < array의 길이 < 100
# 0 ≤ array의 원소 < 1000

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


# def solution(array):
#     while len(array) != 0:
#         for i, a in enumerate(set(array)):
#             array.remove(a)
#         if i == 0: return a
#     return -1

print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))