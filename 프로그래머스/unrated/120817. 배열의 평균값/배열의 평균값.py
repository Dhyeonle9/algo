def solution(numbers):
    if 1<= len(numbers) <= 100:
        if 1<= min(numbers) and max(numbers)<= 1000:    
            answer = sum(numbers) / len(numbers)
    return answer