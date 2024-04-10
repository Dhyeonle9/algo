# import sys

# sys.stdin = open('input.txt')
# n = int(input())
# number = list(map(int, sys.stdin.readline().split()))
# res = [-1] * n
# stack = []

# stack.append(0)
# for i in range(1, n):
#     while stack and number[stack[-1]] < number[i]:
#         res[stack.pop()] = number[i]
#     stack.append(i)

# print(res)

import sys

sys.stdin = open('input.txt')
n = int(input())
number = list(map(int, sys.stdin.readline().split()))
res = ['-1'] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and number[stack[-1]] < number[i]:
        res[stack.pop()] = str(number[i])
    stack.append(i)

print(' '.join(res))