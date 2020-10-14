#QUEUE
class queue:
    def __init__(self, quantum):
        self.head = self.tail = 0
        self.MAX = 100000
        self.q = quantum
        self.Q = [0] * self.MAX

    def isEmpty(self):
        return self.head == self.tail

    def isFull(self):
        # リング状で見たとき最後尾＋１でheadと同じ位置に
        return self.head == (self.tail + 1) % self.MAX

    def enqueue(self, x):
        if self.isFull():
            print("OF")
        self.Q[self.tail] = x
        if self.tail + 1 == self.MAX:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.isEmpty():
            print("UF")
        x = self.Q[self.head]
        if self.head + 1 == self.MAX:
            self.head = 0
        else:
            self.head += 1
        return x

    def roundRobin(self):
        Done = []
        elapsedTime = 0

        while 1:
            if self.isEmpty():
                break

            key, value = self.dequeue().split()
            if int(value) - self.q > 0:
                value = int(value) - self.q
                self.enqueue(f"{key} {value}")
                elapsedTime += self.q #クオンタム時間を経過時間に追加
            else:
                elapsedTime += int(value)#value時間を経過時間に追加
                Done.append(f"{key} {elapsedTime}")

        return Done


n, q = map(int, input().split())

_ = queue(q)

# プロセス入力
for i in range(n):
    _.enqueue(input())

for x in _.roundRobin():
    print(x)
