T = []

W = input()
while 1:

    # 空白で区切られた文字列をリストに一時保存
    line = list(map(str, input().split()))

    # END_OF_FILEのみであるときbreak
    if 'END_OF_TEXT' == line[0]:
        break

    # lineの要素を小文字にしてTに加える
    else:
        T.extend(map(str.lower, line))

# TリストにWがいくつ含まれているか
print(T.count(W))
