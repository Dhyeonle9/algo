# import heapq

# def solution(operations):
#     answer = []
#     heap = []
#     for op in operations:
#         o, num = op.split()
#         num = int(num)

#         if o == 'I':
#             heapq.heappush(heap, num)
#         elif o == 'D':
#             if num == 1 and len(heap)>0:
#                 heap.remove(heap[-1])
#             elif num == -1 and len(heap)>0:
#                 heapq.heappop(heap)

#     if len(heap)!= 0:
#         answer = [heap[-1], heapq.heappop(heap)]
#     else: 
#         answer = [0, 0]
#     return answer

import heapq

def solution(operations):
    answer = []
    heap = []
    for op in operations:
        o, num = op.split()
        num = int(num)

        if o == 'I':
            heapq.heappush(heap, num)
        elif o == 'D':
            if num == 1 and len(heap)>0:
                heap.remove(max(heap))
            elif num == -1 and len(heap)>0:
                heapq.heappop(heap)

    if len(heap)!= 0:
        answer = [max(heap), heapq.heappop(heap)]
    else: 
        answer = [0, 0]
    return answer