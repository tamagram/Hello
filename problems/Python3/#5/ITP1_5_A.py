while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for j in range(H):
        for i in range(W):
            print('#', end='')  # end=''で改行をoff
        print()  # print()で改行
    print()  # データセットごとの空行