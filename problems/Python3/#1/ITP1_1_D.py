S = int(input())
h = S // 60 ** 2
m = S % 60 ** 2 // 60
s = S % 60

# f文字列(f-string)を活用して、フォーマット済みの文字列リテラルを生成
print(f"{h}:{m}:{s}")
