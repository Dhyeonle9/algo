import sys
from collections import Counter

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
count = [0]*1000001
stack = []
res = [-1 for _ in range(N)]

for i in num: 
    count[i] += 1

for j in range(N):
    while stack and count[num[stack[-1]]] < count[num[j]]:
        res[stack.pop()] = num[j]
    stack.append(j)

print(*res)
