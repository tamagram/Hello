S = int(input())
h = S // 60 ** 2
m = S % 60 ** 2 // 60
s = S % 60
print(f"{h}:{m}:{s}")