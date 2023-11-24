def solution(board, moves):     
    answer = 0
    board_c = list(map(list, zip(*board)))
    temp = []
    
    for move in moves:
        for i in range(len(board_c[move-1])):
            if board_c[move-1][i] != 0:
                temp.append(board_c[move-1][i])
                board_c[move-1][i] = 0
                break
                
        if len(temp) >=2 and temp[-2] == temp[-1]:
            del temp[-2:]
            answer += 2
            
    return answer
