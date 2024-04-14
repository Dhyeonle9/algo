import sys

sys.stdin = open('input.txt')

line = input().split()

print(int(line[0]+line[1])+int(line[2]+line[3]))