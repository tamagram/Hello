n, m = map(int, input().split())

# 今までの配列のcoding方法とは違う線形代数
# iをindexではなく行数としjを行数ではなく列数とする
# n*m行列
A = [[0 for j in range(m)] for i in range(n)]
# m*1の列ベクトル
b = [[0 for k in range(1)] for j in range(m)]

#n*m行列の入力
for i in range(n):

    # index0~mの間の要素を変更する
    # indexは,1,2,0,3,の『,』を番号で表したものであることをこの時知った
    A[i][:m] = map(int, input().split())

#m*1列ベクトルの入力
for j in range(m):
    b[j][0] = int(input())

#Ab列ベクトルを出力
for i in range(n):
    c = 0
    for j in range(m):
        c += A[i][j] * b[j][0]
    print(c)
