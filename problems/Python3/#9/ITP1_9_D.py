s = list(input())
q = int(input())

for i in range(q):

    # 命令をlistで分けておく
    # tに余分な要素をzip
    order, a, b, *t = input().split()
    a = int(a)
    b = int(b)

    if order == 'print':
        print(''.join(s[a: b + 1]))

    # reversedは逆順を取り出す
    elif order == 'reverse':

        s[a: b + 1] = reversed(s[a: b + 1])

    elif order == 'replace':

        s[a: b + 1] = ''.join(t)
