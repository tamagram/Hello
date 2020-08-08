# バブルソート
def bubbleSort(A, N):
    count = 0

    flag = 1

    while flag:
        flag = 0

        # 要素すべて(N-1から1)
        for j in range(N - 1, 0, -1):

            # 逆順があるときに入れ替えとflagを真にしてループを継続させる
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]
                flag = 1

                count += 1

    # 後の"\n".joinで結合するためリストに
    return [" ".join(map(str, A)), count]


n = int(input())
a = list(map(int, input().split()))

print("\n".join(map(str, bubbleSort(a, n))))
