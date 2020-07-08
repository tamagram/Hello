while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        for j in range(W):

            #'.'で枠内を埋める(論理積)
            if 0 < i < H - 1 and 0 < j < W - 1:
                print('.', end='')
            #'#'で枠を作る(否定論理積)
            else:
                print('#', end='')
                
        print()
    print()
