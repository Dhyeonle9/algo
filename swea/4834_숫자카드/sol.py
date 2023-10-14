import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = input()

    count = [0 for i in range(10)]

    for n in numbers:
        count[int(n)] += 1

    result = 0

    for i in range(len(count)):
        if result <= count[i]:
            result = count[i]
            idx = i
            
    print(f'#{tc} {idx} {result}')

