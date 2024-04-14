import sys

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    result = (x * y) // gcd(x, y)
    return result

n = int(input())

for i in range(n):
    x, y = map(int, input().split())


    print(lcm(x, y))