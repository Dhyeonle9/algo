import sys
from itertools import combinations
sys.stdin = open('input.txt')

# 0.18216s

# T = int(input())
# A = list(range(1,13))

# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     count = 0
#     for i in range(1<<len(A)):
#         A_set = []
#         for j in range(len(A)):
#             if i & (1<<j):
#                 A_set.append(A[j])

#         if len(A_set) == N and sum(A_set) == K:
#             count += 1
#     print(f'#{tc} {count}')

# # 0.17402s
# T = int(input())
# A = list(range(1,13))

# set_list = []

# for i in range(1<<len(A)):
#     A_set = []
#     for j in range(len(A)):
#         if i & (1<<j):
#             A_set.append(A[j])
#     set_list.append(A_set)

# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     count = 0
#     for i in range(len(set_list)):
#         if len(set_list[i]) == N and sum(set_list[i]) == K:
#             count +=1       
#     print(f'#{tc} {count}')

# 0.153s
# from itertools import combinations

T = int(input())
A = list(range(1,13))

for tc in range(1, T+1):
    N, K = map(int, input().split())
    count = 0
    set_list = list(combinations(A,N))
    for i in range(len(set_list)):
        if len(set_list[i]) == N and sum(set_list[i]) == K:
            count +=1       
    print(f'#{tc} {count}')

