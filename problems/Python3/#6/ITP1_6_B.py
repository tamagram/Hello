n = int(input())

cards = [[False for i in range(13)] for j in range(4)]
pattern = ['S', 'H', 'C', 'D']
# リストをFalseで初期化しpatternをあらかじめ用意する
# {
#  S[False,False,False,False,False,False,False,False,False,False,False,False,False],
#  H[False,False,False,False,False,False,False,False,False,False,False,False,False],
#  C[False,False,False,False,False,False,False,False,False,False,False,False,False],
#  D[False,False,False,False,False,False,False,False,False,False,False,False,False],
# }

for judge in range(n):
    ch, rank = input().split()

    # cards[i][j]の場所をTrueに変える
    # pattern.index(ch)ではpatternリスト内からchと同じ要素のindex(要素番号)を返している
    cards[pattern.index(ch)][int(rank)-1] = True

# cardsのindexは0~3まであるのでその分繰り返す
# enumerateでcardsリストの要素(S,H,C,D)をchに代入
for j, ch in enumerate(cards):

    #cardの要素をrankに代入しその要素数だけ繰り返す
    for i, rank in enumerate(ch):
        if cards[j][i] == False:
            print(f'{pattern[j]} {i+1}')

    # rangeでは繰り返す回数をそのまま書き込むがenumerateでは要素数だけ繰り返すので注意
    # enumerate関数を使うことでindexとリストの要素を取得できる
