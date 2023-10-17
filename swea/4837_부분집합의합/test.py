numbers = list(range(1,5))

n = len(numbers) # n = 5
# 모든 경우의 수만큼 반복
for i in range(1<<n): # shift 연산자, range(2**n)과 같다.

    temp = []
    # n가지 원소가 있는지없는지 분기처리
    for j in range(n):

        # print(i, bin(i<<j))
        # 해당 자리에 데이터가 있는지 없는지 확인
        # 있으면 해당번째 요소를 넣음
        if i & (1<<j): 
            temp.append(numbers[j])
    print(temp)
