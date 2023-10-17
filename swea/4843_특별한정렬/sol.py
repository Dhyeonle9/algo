import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = []
    arr.sort()

    for i in range(5):
        result.append(arr[-1])
        del arr[-1]
        result.append(arr[0])
        del arr[0]
    
    temp = list(map(str, result))
    result = ' '.join(temp)
    print(f'#{tc} {result}')
