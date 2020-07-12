r, c = map(int, input().split())
# 要素数+1,行数+1
table = [[0 for j in range(c + 1)] for i in range(r + 1)]

for i in range(r):
    # (0~c-1)<c
    table[i][:c] = map(int, input().split())

for i in range(r):
    for j in range(c):

        # (0~c-1)+1の要素に加算していき右側に表示される
        # (0~r-1)+1のリストに加算していき下側に表示される
        table[i][c] += table[i][j]
        table[r][j] += table[i][j]

    # 右側の結果を加算
    table[r][c] += table[i][c]

# リストごとに結合し出力
for i, r in enumerate(table):
    print(' '.join(map(str, r)))
