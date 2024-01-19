import heapq

def solution(jobs):
    now = 0
    time = 0
    leng = len(jobs)
    jobs.sort(key = lambda x:x[1])
    
    while len(jobs) > 0:
        for i, t in jobs:
            if i <= now:
                jobs.remove([i, t])
                now += t-1
                time += now - i +1
                break
        now+=1
    return time//leng