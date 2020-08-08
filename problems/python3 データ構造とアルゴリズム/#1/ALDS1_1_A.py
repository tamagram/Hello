# 挿入ソート
def insertionSort(A, N):

    # 要素分繰り返す1 <= i < N
    for i in range(1, N):

        # 変化を出力(ソート処理とは直接関係ない)
        print(" ".join(map(str, A)))

        # ソートするときに詰めていくため取り出しておく
        v = A[i]
        j = i - 1

        # vより手前の値が大きければ詰めていく
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1

        # 手前の値が小さければそこに落ち着く
        A[j + 1] = v


N = int(input())

A = list(map(int, input().split()))

insertionSort(A, N)

# 最終行
print(" ".join(map(str, A)))
