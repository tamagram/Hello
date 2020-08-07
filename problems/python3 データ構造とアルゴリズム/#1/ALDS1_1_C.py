# 素数 Prime Numbers O(√x)
# 合成数の性質を利用
def isprime(x):

    i = 2
    # 2~√xまで
    while i <= x ** (1 / 2):

        # 割り切れるものがあれば素数でない
        if x % i == 0:
            return 0
        i += 1
    return 1


n = int(input())

count = 0
for _ in range(n):
    X = int(input())
    count += isprime(X)

print(count)
