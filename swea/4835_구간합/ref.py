import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    min_total = 1000000
    max_total = 0
    # 구간합을 구하기 위한 i (시작접)
    for i in range(0, N-M+1):
        total = 0

        for j in range(M):
            total += numbers[i+j]
        
        if total < min_total:
            min_total = total
        if total > max_total:
            max_total = total
    result = max_total - min_total
     
    print(f'#{tc} {result}')