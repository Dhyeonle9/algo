import sys

N = int(input())
input_list = list(input().strip())
num = {}
stack = []
for i in range(N):
    num[i]=int(input())

for c in input_list :
  if c in ['+', '-', '/', '*'] :
    b = stack.pop()
    a = stack.pop()
    if c == '+' :
      a += b
    elif c == '-' :
      a -= b
    elif c == '/' :
      a /= b
    else :
      a *= b
    stack.append(a)
  else :
    stack.append(num[ord(c)-ord('A')])

print('{:.02f}'.format(stack[0]))
