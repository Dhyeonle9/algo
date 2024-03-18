# 시간초과
# import sys

# sys.stdin = open('input.txt')

# string = list(input())
# cursor = len(string)

# for i in range(int(input())):
#     com = str(input()).split()
#     if com[0] == 'P':
#         string.insert(cursor, com[1])
#         cursor += 1
#     elif com[0] == 'L':
#         if cursor > 0:
#             cursor -= 1
#     elif com[0] == 'D':
#         if cursor < len(string):
#             cursor += 1
#     else:
#         if cursor > 0:
#             string.remove(string[cursor-1])
# print(''.join(string))

# stack
import sys
# input  = sys.stdin.readline
sys.stdin = open('input.txt')

string = list(str(input()))
stack = []
n = int(input())
for i in range(n):
    com = input().split()
    if com[0] == 'P':
        string.append(com[1])
    elif com[0] == 'L':
        if string:
            stack.append(string.pop())
    elif com[0] == 'D':
        if stack:
            string.append(stack.pop())
    else:
        if string:
            string.pop()
print(''.join(string)+''.join(list(reversed(stack))))


# # deque

# import sys
# from collections import deque

# # input  = sys.stdin.readline
# sys.stdin = open('input.txt')
# string = deque(list(input().split()))
# str_deq = deque()
# cursor = int(input())

# for i in range(cursor):
#     com = input().split()

#     if com[0] == 'L':
#         if len(string) > 0:
#             str_deq.appendleft(string.pop())

#     elif com[0] == 'D':
#         if len(str_deq) > 0 :
#             string.append(str_deq.popleft())

#     elif com[0] == 'B':
#         if len(string) > 0:
#             string.pop()
#     else:
#         string.append(com[1])

# print(''.join(string) + ''.join(str_deq))
