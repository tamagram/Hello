# ミュータブルだと楽（単純な変数だと関数で上書きできない）
# 逆ポーランド
class calculation:
    def __init__(self):
        self.top = 0
        self.MAX = 200
        self.stack = [0] * self.MAX

    def isEnpty(self):
        return self.top == 0

    def isFull(self, MAX):
        return self.top >= MAX - 1

    def push(self, x):
        if self.isFull(self.MAX):
            print("OF")
        self.stack[self.top] = x
        self.top += 1

    def pop(self):
        if self.isEnpty():
            print("UF")
        self.top -= 1
        return self.stack[self.top]


_ = calculation()
for x in input().split():
    if x == "+":
        _.push(_.pop() + _.pop())
    elif x == "-":
        _.push(-(_.pop() - _.pop()))
    elif x == "*":
        _.push(_.pop() * _.pop())
    elif x == "/":
        _.push(1 / (_.pop() / _.pop()))
    else:
        _.push(int(x))
print(_.stack[0])
