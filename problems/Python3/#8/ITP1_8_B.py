while True:
    # 整数を一つずつリストへ
    x = list(map(int, input()))

    # 0一つだけの時終了
    if x[0] == 0 and len(x) == 1:
        break

    # xsumにリスト内の整数を加算し出力
    xsum = 0
    for i in range(len(x)):
        xsum += x[i]
    print(xsum)
