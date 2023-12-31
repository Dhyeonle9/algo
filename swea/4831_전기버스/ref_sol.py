# A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
 
# [예시]
# 다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.

# [입력]
# 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
 
# [출력]
# #과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.


import sys
sys.stdin = open('input.txt')

# T
# K: 한번에 이동가능한 정류장 수, N: 종점 정류장, M: 충전기 수
# 충전기 설치된 정류장 번호

T = int(input())
for tc in range(1, T+1):
    K, N, M = list(map(int, input().split(' ')))
    
    bus_stop = list(map(int, input().split(' ')))
    
    count = 0
    now = 0

    # 충전할 필요가 없이 바로 도착하는 경우
    if K >= N:
        count = 0

    # 충전해야하는 경우
    else :
        # 버스가 아직 종점에 도착하지 않았다면 계속 반복
        while now < N:
            # 현재위치(now)를 기준으로 최대로 갈 수 있는 범위를 찾는다.
            for i in range(now+K, now, -1):
                # 1. 최대범위가 종점을 넘는경우
                if i >= N:
                    now = N
                    break
                # 2. 최대범위가 종점을 넘지 않는 경우

                if i in bus_stop:
                    count += 1
                    now = i
                    break
            # 현재 위치에서 최대 거리까지 다 확인을 했는데 충전소가 없다면 => 도착 불가능
            else:
                count = 0
                now = N   

    print(f'#{tc} {count}')

# import sys
# sys.stdin = open('input.txt')

# T = int(input())

# for tc in range(1, T+1):

#     K, N, M = list(map(int, input().split()))  #설명에 나와있듯 첫번째는 K(1회 충전 당 이동할 수 있는거리), N(도착해야하는 위치), M(정류소 갯수)

#     charge_station = list(map(int, input().split()))  #charge_station을 호출했으니 사실상 M이라는 변수는 이제 생각 안해도 될듯

#     count = 0

#     current = 0

#     while current + K < N:  #현재위치에서 한번에 이동 가능한 K를 합한 값이 내가 도착해야하는 위치보다 클 때 루프 종료

#         for move in range(K, 0, -1): #K만큼 움직이다 충전소가 있는 K-(가장 작은 수)에 충전소가 있으면 충전을 해야하니 K~0까지 -1
    
#             if (current + move) in charge_station: 
#                 current += move                     #현재위치에서 충전소까지 이동했으니 현재 위치는 충전소이다.
#                 count += 1                          #충전소에서 충전을 했으면 1회 count

#                 break
#         else:                                      #움직이는 거리 안에 충전소가 없다면 count x = 도착 x
#             count = 0
#             break
    
#     print(f'#{tc} {count}')

