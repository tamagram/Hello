n = int(input())

# mapで空白で区切られた文字列をintに
# listで配列に
a = list(map(int, input().split()))

#listであるaを逆順に
a.reverse()

#end=' 'を' 'と指定することができ改行offかつ先頭空白
#joinでlistを結合していく
#strに変換
print(' '.join(map(str, a)))

#結合時に改行は行われず、出力時に改行される
#なので最後の改行print()は要らない