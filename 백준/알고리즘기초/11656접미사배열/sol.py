import sys

sys.stdin = open('input.txt')
w = input()
l = []
for i in range(len(w)):
    l.append(w[i:])
l.sort()

for j in l:
    print(j)