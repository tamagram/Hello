n, m, l = map(int, input().split())

A = []
B = []
C = [[0 for k in range(l)] for i in range(n)]

#Aの行列リスト
for i in range(n):
    A.append(list(map(int, input().split())))
#Bの行列リスト
for j in range(m):
    B.append(list(map(int, input().split())))

#Aの行とBの列を加算していく
for i in range(n):
    for j in range(m):
        for k in range(l):
            C[i][k] += A[i][j] * B[j][k]

for i in range(n):
    print(' '.join(map(str, C[i])))
