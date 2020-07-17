while 1:
    
    cards = input()

    if cards == '-':
        break

    m = int(input())

    h = 0

    for i in range(m):
        h += int(input())

    #シャッフルしてループした分を除き
    h = h % len(cards)

    #入力したcardsを連結
    ling = cards + cards

    #前の問題のようにある範囲の文字列を抽出
    print(ling[h: h + len(cards)])
