# 平均、中央値、最頻値、分散、標準偏差
import statistics

while 1:
    n = float(input())

    if n == 0:
        break

    s = list(map(float, input().split()))

    # 標準偏差(個々の値がどれだけ平均とずれているか)
    print(f"{statistics.pstdev(s):.8f}")
