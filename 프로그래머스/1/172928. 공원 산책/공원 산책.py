def solution(park, routes):
    loc = [0, 0]
    move = {
        'E': [0, 1],
        'W': [0, -1],
        'S': [1, 0],
        'N': [-1, 0],
    }
    for i, road in enumerate(park):
        if 'S' in road:
            loc = [i, road.find('S')]
            break
            
    for route in routes:
        d, s = route.split()
        cur_loc = loc
        for i in range(int(s)):
            new_loc = [loc[0] + move[d][0], loc[1] + move[d][1]]
            if 0<=new_loc[0]<=len(park)-1 and 0<=new_loc[1]<=len(park[0])-1 and park[new_loc[0]][new_loc[1]] != 'X':
                    loc = [new_loc[0], new_loc[1]]
            else:
                loc = cur_loc
                break
                    
    return loc