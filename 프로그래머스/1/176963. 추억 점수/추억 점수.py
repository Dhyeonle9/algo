def solution(name, yearning, photo):
    answer = []
    ny = {nam: yearn for yearn, nam in zip(yearning, name)}
    for pho in photo:
        score = 0
        for person in pho:
            if person in ny:
                score += ny[person]
        answer.append(score)                          
            
    return answer
        