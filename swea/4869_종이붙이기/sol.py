import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())//10
    paper = [1, 3] 
    for n in range(2, N):
        paper.append(paper[n-1] + paper[n-2]*2)
    
    print(f'#{tc} {paper[N-1]}')

