import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

def search(idx):
    if idx >= N:
        print(result)
        return
    # 모든 경우의 수 탐색
    for i in range(N):
        result.append(numbers[idx][i])
        check_list[i] = True
        search(idx+1)
        result.pop()
        check_list[i] = False
for tc in range(1, T+1):
    N = int(input())
    numbers = []
    for _ in range(N):
        number= list(map(int, input().split()))
        numbers.append(number)

    result = []
    check_list = [False] * N
    search(0)
