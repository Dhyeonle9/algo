import sys
sys.stdin = open('input.txt', encoding='UTF-8')

man1 = input()
man2 = input()

# 1번

# if man1 == man2:
#     print('Result : Draw')

# else:
#     if man1 == '가위':
#         if man2 == '바위':
#             print('Result : Man2 Win!')
#         else:
#             print('Result : Man1 Win!')
#     if man1 == '바위':
#         if man2 == '보':
#             print('Result : Man2 Win!')
#         else:
#             print('Result : Man1 Win!')
#     if man1 == '보':
#         if man2 == '가위':
#             print('Result : Man2 Win!')
#         else:
#             print('Result : Man1 Win!')


# 2번
rsp = ['가위', '바위', '보']

man1_idx = rsp.index(man1)
man2_idx = rsp.index(man2)

result = man1_idx - man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
else:
    # if reult == -1:
    #     print('Result : Man2 Win!')
    # else:
    #     print('Result : Man1 Win!')
    print(f'Result : Man{result+3} Win!')