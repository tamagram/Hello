a, b = map(int, input().split())
d = int(a / b)
r = int(a % b)
f = a / b

# {f:.5f}でfの値を小数点第5位まで表示
print(f'{d} {r} {f:.5f}')
