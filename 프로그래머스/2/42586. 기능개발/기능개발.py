def solution(progresses, speeds):
    answer = []
    cnt = 0
    while len(progresses)>0:
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            for i in range(len(progresses)):
                progresses[i] = progresses[i] + speeds[i]
    answer.append(cnt)
    return answer