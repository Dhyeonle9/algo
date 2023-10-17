import sys
sys.stdin = open('input.txt')


for TC in range(10):

    tc = int(input())
    matrix = []
    for i in range(100):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)

    max = 0

    for i in range(100):
        sum = 0
        for j in range(100):
            sum += matrix[i][j]
        if max < sum:
            max = sum


    for j in range(100):
        sum = 0
        for i in range(100):        
            sum += matrix[i][j]
        if max < sum:
            max = sum


    for i in range(100):
        sum = 0
        sum += matrix[i][i]
        if max < sum:
            max = sum


    for i in range(100):
        sum = 0
        sum+= matrix[i][99-i]
        if max < sum:
            max = sum
 
    print(f'#{tc} {max}')
