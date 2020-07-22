import math

# 可読性を高めるだけ
sin, cos = math.sin, math.cos

a, b, C = map(int, input().split())

# ラジアン
radC = math.radians(C)

S = 1 / 2 * a * b * sin(radC)
# 余弦定理
L = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(radC))
h = b * sin(radC)

# /nで改行しながら出力
print(f"{S:.8f}\n{L:.8f}\n{h:.8f}")
