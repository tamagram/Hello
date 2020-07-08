# 空白で区切られた文字列をa,bに格納
a, b = map(int, input().split())

if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')
