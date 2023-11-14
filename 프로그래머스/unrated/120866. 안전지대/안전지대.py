def solution(board):
    answer = 0
    n = len(board)
    danger = [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for x, y in danger:
                    if (0<=i+x<n and 0<=j+y<n) and board[i+x][j+y] == 0:
                        board[i+x][j+y] = 2
    for i in board:
        answer += i.count(0)
    return answer
                        