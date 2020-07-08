l = input()

# mapではリストのようなオブジェクトに含まれる各要素に対して、統一された変換処理を施す
a, b = map(int, l.split())

print(a * b, 2 * a + 2 * b)
