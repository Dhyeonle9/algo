import sys
line = list(map(int, input().split()))
A, B, C = line[0], line[1], line[2]
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)