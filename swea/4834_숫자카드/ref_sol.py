import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    numbers = input()

    counter = [0 for i in range(10)]

    for n in numbers:
        counter[int(n)] += 1

    card_count = 0
    card_number = 0
    
    for idx, value in enumerate(counter):
        if card_count <= value:
            card_count = value
            card_number = idx

    print(f'#{tc} {card_number} {card_count}')