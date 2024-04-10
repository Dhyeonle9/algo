import sys

line = input().split()
A, B, C = int(line[0]), int(line[1]), int(line[2])
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)