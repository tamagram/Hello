# mathモジュールの読み込み
import math

x1, y1, x2, y2 = map(float, input().split())

# math.sqrt()で平方根を求める
print(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
