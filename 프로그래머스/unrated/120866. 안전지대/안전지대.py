# def solution(board):
#     answer = 0
#     n = len(board)
#     danger = [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == 1:
#                 for x, y in danger:
#                     if (0<=i+x<n and 0<=j+y<n) and board[i+x][j+y] == 0:
#                         board[i+x][j+y] = 2
#     for i in board:
#         answer += i.count(0)
#     return answer
def solution(board):
    n = len(board)
    mat = [[0]*(n+2) for _ in range(n+2)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                mat[i][j] = 1
                mat[i][j+1] = 1
                mat[i][j+2] = 1
                mat[i+1][j] = 1
                mat[i+1][j+1] = 1
                mat[i+1][j+2] = 1
                mat[i+2][j] = 1
                mat[i+2][j+1] = 1
                mat[i+2][j+2] = 1

    count = 0
    for i in range(n+2):
        for j in range(n+2):
            if 0<i<n+1 and 0<j<n+1 and mat[i][j] == 0:
                count += 1
    
    return count