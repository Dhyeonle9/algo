import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    A, B = 0, 0
    get = 0
    l = 1
    r = P

    while get == 0:
        if Pa != l and Pa != r:
            A += 1
            if Pa < int((l+r)/2):
                r = int((l+r)/2)
            elif Pa > int((l+r)/2):
                l = int((l+r)/2)
            else:
                get += 1
            # print(l, r, A, Pa, get)
        else:
            get += 1
    get = 0
    l = 1
    r = P
    while get == 0:
        if Pb != l and Pb != r:
            B += 1
            if Pb < int((l+r)/2):
                r = int((l+r)/2)
            elif Pb > int((l+r)/2):
                l = int((l+r)/2)
            else:
                get += 1
            # print(l, r, A, Pa, get)
        else:
            get += 1        
    print(f'#{tc} A') if A < B else (print(f'#{tc} B') if A > B else print(f'#{tc} 0'))