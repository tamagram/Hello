# 選択ソート O(n**2)
def selectionSort(A, N):

    count = 0

    for i in range(N):
        minj = i

        # 未ソートの範囲
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j

        if minj != i:
            A[i], A[minj] = A[minj], A[i]

            count += 1

    return [" ".join(map(str, A)), count]


n = int(input())
a = list(map(int, input().split()))

print("\n".join(map(str, selectionSort(a, n))))

