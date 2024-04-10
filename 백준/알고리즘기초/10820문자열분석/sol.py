# import sys

# sys.stdin = open('input.txt')
# while True :
#     try :
#         lst = list(input())
#         lower , upper, num, blank = 0,0,0,0
#         for i in range(len(lst)) :
#             if lst[i] == " " :
#                 blank += 1
#             elif 65 <= ord(lst[i]) <= 90 :
#                 upper += 1
#             elif 97 <= ord(lst[i]) <= 122 :
#                 lower += 1
#             else :
#                 num += 1
#         print(lower,upper,num,blank)
#     except EOFError :
#         break

import sys

sys.stdin = open('input.txt')
while True :
    line = sys.stdin.readline().rstrip('\n')
    
    if not line:
        break   
    
    lower , upper, num, blank = 0,0,0,0
    for i in range(len(line)) :
            if line[i] == " " :
                blank += 1
            elif line[i].isupper() :
                upper += 1
            elif line[i].islower() :
                lower += 1
            else :
                num += 1
    print(lower,upper,num,blank)
