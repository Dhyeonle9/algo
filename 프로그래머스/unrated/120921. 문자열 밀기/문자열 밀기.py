def solution(A, B):
    for i in range(len(A)):
        if A[-i:]+A[:-i] == B:
            return i
    else:
        return -1

    
# find 함수활용해보려했으나 실패...