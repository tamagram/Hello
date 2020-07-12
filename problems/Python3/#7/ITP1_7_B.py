while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    combi = 0

    # 1<=i<n+1の範囲
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n + 1):

                # 重複回避
                if i >= j or j >= k:
                    continue

                elif i + j + k == x:
                    combi += 1
    print(combi)
