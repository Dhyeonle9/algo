def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])//2):
            if board[i][j] == 1:
                if -len(board[0])//2 + 1 <= i <= len(board[0])//2 - 1 and -len(board[0])//2 + 1 <= j <= len(board[0])//2 - 1:
                       board[i-1:i+2][j-1:j+2] = 1   

    return board.count(0)