n = int(input())

# 3次元配列を定義
A = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

# 適当な変数つけてn回繰り返す
for update in range(n):
    b, f, r, v = map(int, input().split())

    # A[k][j][i]の順
    # v人を追加
    A[b-1][f-1][r-1] += v

# Aの要素をbに代入しその要素数だけ繰り返す
for k, b in enumerate(A):

    # 開始時のみスキップすることで最後に区切りを残さない
    if k != 0:
        k == print('#' * 20)

    # bの要素をfに代入しその要素数だけ繰り返す
    for j, f in enumerate(b):

        # joinで要素を結合し文字列に変換
        # 先頭空白'',要素間隔' ',文字列出力時に改行
        print('', ' '.join(map(str, f)))
