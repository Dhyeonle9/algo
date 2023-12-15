from collections import deque

def solution(priorities, location):
    answer = [] # 실행된 프로세스
    priorities = deque((i, j) for i, j in enumerate(priorities))
    while priorities:
        temp = priorities.popleft()
        # 우선순위가 더 높은 프로세스가 하나라도 있으면 큐에 다시 추가 / 아니면 해당 프로세스 실행
        if priorities and any(temp[1] < p[1] for p in priorities):
            priorities.append(temp)
        else:
            answer.append(temp)
    
    # location 실행 순서 찾기
    for i in answer:
        if i[0] == location:
            return answer.index(i)+1