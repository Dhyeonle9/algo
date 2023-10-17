import sys
sys.stdin = open('input.txt')

# 0.14788초
T = int(input())

def coloring(x1, y1, x2, y2, color):
    count = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if arr[x][y] == 0:
                arr[x][y] += color
            else:
                count +=1
    return count

for tc in range(1, T+1):

    N = int(input())
    cnt = 0
    arr = [[0] * 10 for i in range(10)]
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        cnt += coloring(r1, c1, r2, c2, color)

    print(f'#{tc} {cnt}')

# 0.14990s 
# T = int(input())

# for tc in range(1, T+1):

#     N = int(input())
#     cnt = 0
#     arr = [[0] * 10 for i in range(10)]
#     for n in range(N):
#         r1, c1, r2, c2, color = map(int, input().split())

#         for x in range(r1, r2+1):
#             for y in range(c1, c2+1):
#                 arr[x][y] += color
#                 if arr[x][y] == 3:
#                     cnt +=1

#     print(f'#{tc} {cnt}')
            