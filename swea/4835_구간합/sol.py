import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split(' '))
    numbers = list(map(int, input().split(' ')))
    max = numbers[0]
    min = numbers[0]

    for n in range (N-M, 0, -1):
        for i in range(n):
            if numbers[i]+numbers[i+1]+numbers[i+2] > max:
                max = numbers[i]+numbers[i+1]+numbers[i+2]
            if numbers[i]+numbers[i+1]+numbers[i+2] < min:
                min = numbers[i]+numbers[i+1]+numbers[i+2]
    print(min, max)