# heap은 리스트와 달리 push, pop 이후 정렬이 자동으로 됨
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 리스트를 바로 heap으로 변환, O(N)
    while scoville[0] < K:
        temp = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, temp)
        answer += 1
        if len(scoville) < 2 and scoville[0] < K:
            return -1
    return answer