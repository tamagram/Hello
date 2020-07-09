while True:
    h, w = map(int, input().split())
    if h + w == 0:
        break
    for j in range(h):
        for i in range(w):

            # この場合i+jが偶数のときに文字を打つことでチェック柄ができる
            if (i+j) % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')

        print()
    print()
