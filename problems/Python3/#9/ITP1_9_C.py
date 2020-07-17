n = int(input())

# 得点
P1score = P2score = 0

for i in range(n):

    # ターンごとに両者のカードを入力
    P1card, P2card = input().split()

    # そのまま比較できるらしい
    if P1card == P2card:
        P1score, P2score = P1score + 1, P2score + 1
    elif P1card < P2card:
        P2score += 3
    else:
        P1score += 3

print(P1score, P2score)
