a, b, c = map(int, input().split())

# 変数の値を入れ替える
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)
