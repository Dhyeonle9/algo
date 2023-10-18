import sys
sys.stdin = open('input.txt')

# T = int(input())

# for tc in range(1, T+1):

#     N, M = map(int, input().split())
#     array = []

#     for _ in range(N):
#         array.append(list(map(int, input().split())))

#     max = 0

#     for i in range(N-M+1):
#         for j in range(N-M+1):
            
#             sum = 0
#             for k in range(M):
#                 for l in range(M):
#                     sum += array[i+k][j+l]
           
#             if sum > max:
#                 max = sum
#     print(f'#{tc} {max}')

T = int(input())

def find_max(N, M):
    max = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            
            sum = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    sum += array[k][l]
           
            if sum > max:
                max = sum
    return max

for tc in range(1, T+1):

    N, M = map(int, input().split())
    array = []
    
    for _ in range(N):
        array.append(list(map(int, input().split())))

    result = find_max(N, M)
    
    print(f'#{tc} {result}')