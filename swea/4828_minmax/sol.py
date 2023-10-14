import sys

sys.stdin = open('input.txt')

T = int(input())
# bubble sort
# for tc in range(1, T+1):
#     N = int(input())
    
#     numbers = list(map(int,input().split(' ')))
    
#     for n in range(N-1, 0, -1):
#         for i in range(n):
#             if numbers[i] > numbers[i+1]:
#                 numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#     print(f'#{tc} {numbers[-1]-numbers[0]}')

# min max 값 각각 비교
# for tc in range(1, T+1):
#     N = int(input())
    
#     numbers = list(map(int,input().split(' ')))
#     min = 0
#     max = 0
#     for n in range(N):
#         if min ==0:
#             min = numbers[n]
#         else:
#             if min > numbers[n]:
#                 min = numbers[n]
#     for n in range(N):
#         if max ==0:
#             max = numbers[n]
#         else:
#             if max < numbers[n]:
#                 max = numbers[n]
        
#     print(f'#{tc} {max-min}')

# sort 함수 이용
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(f'#{tc} {numbers[-1] - numbers[0]}')