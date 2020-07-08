W, H, x, y, r = map(int, input().split())

# 円の端がそれぞれ0~W,0~Hに収まっているか
if 0 <= x - r and x + r <= W and 0 <= y - r and y + r <= H:
    print('Yes')
else:
    print('No')
