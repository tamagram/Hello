i = 0
a, b, c = map(int, input().split())
while a <= b:

    # 約数を見つけたとき
    if c % a == 0:
        i += 1
    a += 1

print(i)
