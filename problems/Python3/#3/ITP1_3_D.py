i = 0
a, b, c = map(int, input().split())
while a <= b:
    if c % a == 0:
        i += 1
    a += 1
print(i)
