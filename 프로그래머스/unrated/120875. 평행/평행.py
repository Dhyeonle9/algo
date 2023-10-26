from itertools import combinations
def solution(dots):
    arr = list(combinations(dots,2))
    for i in range(len(arr)//2):
        a = (arr[i][0][1]-arr[i][1][1])/(arr[i][0][0]-arr[i][1][0])
        b = (arr[len(arr)-i-1][0][1]-arr[len(arr)-i-1][1][1])/(arr[len(arr)-i-1][0][0]-arr[len(arr)-i-1][1][0])
        if a == b:
            return 1
    else:
        return 0
    
# gradient 함수를 이용해서 풀어보기!
