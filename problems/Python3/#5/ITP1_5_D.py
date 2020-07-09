n = int(input())
# このときrangeは1<=i<n+1なので気を付ける
for i in range(1, n+1):
    x = i

    # 約数3
    if x % 3 == 0:
        print(f' {i}', end='')

    # 桁ごとに3を見つける
    else:
        while x >= 3:
            if x % 10 == 3:
                print(f' {i}', end='')
                break
            x //= 10

# 最後にちゃんと改行する
print()
