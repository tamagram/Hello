while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for j in range(H):
        for i in range(W):

            #'.'で枠内を埋める(論理積)
            if 0 < j < H - 1 and 0 < i < W - 1:
                print('.', end='')
            #'#'で枠を作る(否定論理積)
            else:
                print('#', end='')
                
        print()
    print()
