# この問題はEOFまで読み込む必要があるらしいので
# 例外処理を使う
# EOF入力はCtrl+D

asciiAnumber = 65

# 枠組み
counter = [0 for n in range(26)]
sentence = []

# 1=True
while 1:

    # 例外処理EOF
    try:
        sentence.extend(list(input()))
    except EOFError:
        break

# 文字数だけループ
for i, alphabet in enumerate(sentence):

    # 文字の判定とカウント
    for n in range(26):
        if alphabet == chr(n + asciiAnumber) or alphabet == chr(n + asciiAnumber + 32):
            counter[n] += 1

# countリストにアルファベットを割り当てて出力
for n in range(26):
    print(f'{chr(n + asciiAnumber + 32)} : {counter[n]}')
