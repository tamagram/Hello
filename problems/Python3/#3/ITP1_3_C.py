x, y = map(int, input().split())
while True:
    if x == 0 and y == 0:
        break
    elif x > y:
        x, y = y, x
    print(x, y)
    x, y = map(int, input().split())