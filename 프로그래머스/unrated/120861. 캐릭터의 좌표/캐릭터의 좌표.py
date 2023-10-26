# def solution(keyinput, board):
#     answer = [0, 0]
#     width, length = board[0]//2, board[1]//2
#     for i in keyinput:
#         if i == 'left' and answer[0]-1 >= -width:
#             answer[0] -= 1
#         elif i == 'right'and answer[0]+1 <= width:
#             answer[0] += 1
#         elif i == 'down'and answer[1]-1 >= -length:
#             answer[1] -= 1
#         elif i == 'up' and answer[1]+1 <= length:
#             answer[1] += 1    
#     return answer

def solution(keyinput, board):
    answer = [0, 0]
    temp = [0, 0]
    width, length = board[0]//2, board[1]//2
    move = {'left': [-1, 0],
            'right': [1, 0], 
            'up': [0, 1], 
            'down': [0, -1],
           }
    for key in keyinput:
        temp = [x + y for x, y in zip(answer, move[key])]  
        if abs(temp[0]) > width or abs(temp[1]) > length:
            continue
        else:
            answer = [x + y for x, y in zip(answer, move[key])]                   
    return answer