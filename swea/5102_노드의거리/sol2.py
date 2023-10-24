import sys
from pprint import pprint

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # V: 노드 수, E: 간선 수
    V, E = list(map(int, input().split()))

    nodes = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        node = list(map(int, input().split()))

        start = node[0]
        end = node[1]

        nodes[start][end] = 1
        nodes[end][start] = 1
    # pprint(nodes)
    S, G = list(map(int, input().split()))


    # bfs를 구현하기 위한 queue
    queue = []

    # 거리 계산을 위한 리스트+방문체크
    distance = [0] * (V+1)

    # 시작전 시작 노드를 저장
    now = S

    queue.append(now)
    # 큐가 비어있지 않으면 계속 반복
    while len(queue):
        now = queue.pop(0)
        # now와 연결되어있는 다른 노드를 순회
        for link in range(V+1):
            if nodes[now][link] == 1:
                # 만약 아직 방문하지 않은 node가 있다면
                # if not check_list[link]:
                if distance[link] == False:    
                    queue.append(link)

                    # 이전 노드의 거리 + 1
                    distance[link] = distance[now]+1
    print(f'#{tc} {distance[G]}')
                
        

