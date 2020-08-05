# 最大公約数 GreatestCommonDivisor
def gcd(x, y):

    # ユークリッドの互除法
    if x < y:
        x, y = y, x
    while y > 0:
        r = x % y
        x, y = y, r

    return x

X, Y = map(int, input().split())
print(gcd(X, Y))

