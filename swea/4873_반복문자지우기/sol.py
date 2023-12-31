import sys
sys.stdin = open('input.txt')

# T = int(input())

# for tc in range(1, T+1):
#     text = input()
#     stack = []
#     for char in text:
#         if not stack:
#             stack.append(char)
#         else:
#             if char == stack[-1]:
#                 stack.pop()
#             else:
#                 stack.append(char)
#     print(f'#{tc} {len(stack)}')

T = int(input())

for tc in range(1, T+1):
    text = input()
    stack = []
    for char in text:
        if stack and char == stack[-1]:
            stack.pop()    
        else:
            stack.append(char)
      
    print(f'#{tc} {len(stack)}')
