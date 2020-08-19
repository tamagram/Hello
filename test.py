def insertionSort(A, n, g):

    cntAdd = 0

    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cntAdd += 1
        A[j + g] = v

    return cntAdd


def shellSort(A, n):

    cnt = 0
    G = []
    # ソート間隔h
    h = len(A)

    while h > 0:

        h //= 2
        # カウントとAの並び替え
        cnt += insertionSort(A, n, h)
        G.append(h)

    return len(G), " ".join(map(str, G)), cnt, "\n".join(map(str, A))


n = int(input())
# 改行入力
A = [int(input()) for _ in range(n)]
# タプルの戻り値を改行で出力
print("\n".join(map(str, shellSort(A, n))))
