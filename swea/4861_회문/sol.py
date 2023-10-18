import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(input()))
    
    result = ''
    #가로줄 찾기
    for row in range(N):
        for i in range(N-M+1):
            for k in range(M//2):
                if arr[row][i+k] != arr[row][i+M-k-1]:
                    break
            else:
                result = ''.join(arr[row][i:i+M])
                break
            
    #세로줄찾기
    else:
        for col in range(N):
            for i in range(N-M+1):        
                for k in range(M//2):      
                    if arr[i+k][col] != arr[i+M-k-1][col]:
                        break
                else:
                    for m in range(M):
                        result += arr[i+m][col]
                    break

    print(f'#{tc} {result}')
