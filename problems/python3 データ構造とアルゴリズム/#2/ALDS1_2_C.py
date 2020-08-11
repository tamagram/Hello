def BubbleSort(C, N):
    Flag = 1
    while Flag:
        Flag = 0
        for i in range(N - 1, 0, -1):
            if C[i - 1][1:] > C[i][1:]:
                C[i - 1], C[i] = C[i], C[i - 1]
                Flag = 1

    return C


def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j][1:] < C[minj][1:]:
                minj = j
        if minj != i:
            C[i], C[minj] = C[minj], C[i]
    return C


n = int(input())
c = list(input().split())

# スライスを使ってリストcをコピー(参照回避)
# こうすることにより元のリスト(c)が上書きされなくなる
bSort = " ".join(BubbleSort(c[:], n))
sSort = " ".join(SelectionSort(c[:], n))
# 参照渡しを回避しない場合リストcのBubbleSortの結果がSelectionSortの引数として入ってしまう

print(f"{bSort}\nStable")
print(sSort)
print("Stable") if bSort == sSort else print("Not stable")

