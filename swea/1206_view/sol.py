import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    left = [0, 0]
    right = [0, 0]

    for n in range(2, N-2):
        for i in range(1,3):
            left[i-1] = buildings[n] - buildings[n-i]
            if left[i-1] < 0:
                left[i-1] = 0
            
            right[i-1] = buildings[n] - buildings[n+i]
            if right[i-1] < 0:
                right[i-1] = 0
        result += min(min(left), min(right))
    print(f'#{tc} {result}')