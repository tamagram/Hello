while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break

    # jは0~H-1まで繰り返す
    for j in range(H):
        # iは0~W-1まで繰り返す
        for i in range(W):
            print('#', end='')  # end=''で改行off
        print()  # print()で改行
    print()  # データセットごとの空行