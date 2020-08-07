# 最大利益を求めるO(n)
def profit(n):

    for i in range(n):
        x = int(input())

        # 最小値をセット
        if i == 0:
            minv = x

        else:
            # 最大利益
            if i == 1:
                maxv = x - minv
            else:
                if maxv < x - minv:
                    maxv = x - minv

            # 最小値をリセット(リセットは最大利益計算後)
            if minv > x:
                minv = x

    return maxv


n = int(input())

# 関数内の変数で結構悩んだので
# 繰り返し入力などは関数内で行ったほうがいいかもしれない
p = profit(n)

print(p)
