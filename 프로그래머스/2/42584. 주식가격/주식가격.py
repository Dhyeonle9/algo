from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        temp = prices.popleft()
        time = 0
        for price in prices:
            if temp > price:
                time +=1
                break
            time +=1
        answer.append(time)
    return answer