import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 1000

    for i in range(N):
        check = [[False]*N for _ in range(N)]
        sum = 0
        for j in range(N):
            if not check[i][j]:
                if sum > min_sum:
                    break
                else:
                    sum += arr[i][j]
                    for k in range(N):
                        check[i][k] = True
                        check[k][i] = True   
        if sum < min_sum:
            min_sum = sum        
 
                
    print(min_sum)
