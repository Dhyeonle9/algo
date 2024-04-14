import sys

def get_primes(n):
    # 0과 1은 소수가 아니므로, False 처리
    is_prime = [False, False] + [True] * (n-1)
    primes = []
    # 2부터 n까지의 수에 대해서, 에라토스테네스의 체 알고리즘 적용
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            # i의 배수들은 소수가 아니므로 False 처리
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return primes

# 입력값 처리
sys.stdin.readline()
lst = list(map(int, sys.stdin.readline().split()))

# lst의 최대값까지의 소수 리스트를 구함
primes = get_primes(max(lst))

cnt = 0
# lst에서 소수의 개수를 구함
for i in range(len(lst)):
    if lst[i] in primes:
        cnt += 1

print(cnt)