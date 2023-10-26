# def solution(slice, n):
#     return n // slice + 1 if n % slice else n // slice

def solution(slice, n):
    return ((n - 1) // slice) + 1