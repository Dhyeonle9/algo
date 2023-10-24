import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

def search(idx):
    global sum, min_sum

    if idx >= N:
        if sum < min_sum:
            min_sum = sum
        return
    # 모든 경우의 수 탐색
    for i in range(N):
        if check_list[i] == False:
            sum += numbers[idx][i]
            check_list[i] = True
            search(idx+1)
            sum -= numbers[idx][i]
            check_list[i] = False

            
for tc in range(1, T+1):

    N = int(input())
    numbers = []
    for _ in range(N):
        number= list(map(int, input().split()))
        numbers.append(number)

    result = []
    check_list = [False] * N

    sum = 0
    min_sum = 1000000
    search(0)
    print(min_sum)
