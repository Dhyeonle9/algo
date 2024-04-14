# import sys

# line = input().split()
# A, B, C = int(line[0]), int(line[1]), int(line[2])
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

import sys

sys.stdin = open('input.txt')
line = list(map(int, input().split()))
A, B, C = line[0], line[1], line[2]
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)