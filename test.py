# asciiコードはord('文字'),chr(数値)が使えるらしい

# 大文字と小文字の間にある記号をskip
wordInterval = 6

# list(input())で一文字ずつ分割
s = list(input())
for i, alphabet in enumerate(s):

    alphabet = ord(alphabet)

    # 小文字と大文字を一個ずつ変換
    if 64 < alphabet < 91:
        alphabet += (26 + wordInterval)
    elif 96 < alphabet < 123:
        alphabet -= (26 + wordInterval)
    alphabet = chr(alphabet)

    print(alphabet, end='')
    
print()
