import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    code = input()
    stack = []
    check = 1
    for char in code:    
        if char in '({':
            stack.append(char)
        elif char in ')}':
            if not stack:
                check = 0
                break
            else:
                if char ==')'and stack[-1] == '(':
                    stack.pop()
                
                elif char =='}' and stack[-1] == '{':
                    stack.pop()  
                else:
                    check = 0
                    break
    if stack:
        check = 0

    print(f'#{tc} {check}')
         

# T = int(input())

# for tc in range(1,T+1):
#     code = input()
#     stack = []
#     check = 1
#     for char in code:
        
#         if char in '({':
#             stack.append(char)
#         elif char in ')}':
#             if not stack:
#                 check = 0
#                 break
#             elif char ==')'and stack.pop() != '(':
#                 check = 0
#                 break
#             elif char =='}' and stack.pop() != '{':
#                 check = 0
#                 break   
#     if stack:
#         check = 0

#     print(f'#{tc} {check}')