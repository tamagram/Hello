n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
Abs = []

# 絶対値をリストへ
for i in range(n):
    Abs.append(abs(x[i] - y[i]))

for p in range(1, 4):

    # リスト内包表記で個々の絶対値を処理
    # 絶対値を合算し平方根立方根を求める
    Dxy = sum([i ** p for i in Abs]) ** (1 / p)
    print(f"{Dxy:.6f}")

# チェビシェフ距離は最も離れている成分の絶対値
print(f"{max(Abs):.6f}")
