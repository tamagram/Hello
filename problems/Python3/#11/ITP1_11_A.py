# classを使う
class dice:
    def __init__(self, face):
        self.face = face

    # hoge()で呼び出し可能
    def __call__(self):
        print(self.face[0])

    # class内関数
    # 各インスタンスをselfとして中身を関数によって処理
    def rotate(self, controll):

        # N = [1, 5, 2, 3, 0, 4]
        # S = [4, 0, 2, 3, 5, 1]
        # E = [3, 1, 0, 5, 4, 2]
        # W = [2, 1, 5, 0, 4, 3]

        for swap in controll:
            if swap == "N":
                l = self.face
                self.face = [l[1], l[5], l[2], l[3], l[0], l[4]]
            elif swap == "S":
                l = self.face
                self.face = [l[4], l[0], l[2], l[3], l[5], l[1]]
            elif swap == "E":
                l = self.face
                self.face = [l[3], l[1], l[0], l[5], l[4], l[2]]
            elif swap == "W":
                l = self.face
                self.face = [l[2], l[1], l[5], l[0], l[4], l[3]]


# インスタンスaのfaceに出目のlistを割り当てる
a = dice(list(map(int, input().split())))

controll = input()

a.rotate(controll)

a()
