s = input()
p = input()

# 同じ文字列をくっつけるs=abcのときs*2=abcabc
# 2周するので1週の最後の文字から始まる文も見つけられる

print('Yes' if p in s * 2 else 'No')
