import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    max = 0
    min = 1000000
    result = 0

    
    for n in range (0, N-M+1):
        sum = 0
        for i in range(M):
            sum += numbers[n+i]
        if sum > max:
            max = sum
        if sum < min:
            min = sum
    result = max - min

    print(f'#{tc} {result}')