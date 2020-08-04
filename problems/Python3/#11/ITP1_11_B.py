# classを使う
class dice:
    def __init__(self, face):
        self.face = face

    def searchFace(self, s):

        # N = [1, 5, 2, 3, 0, 4]
        # S = [4, 0, 2, 3, 5, 1]
        # E = [3, 1, 0, 5, 4, 2]
        # W = [2, 1, 5, 0, 4, 3]

        # 4回転
        # タプルを_にすることでUnused variableを避ける
        for _ in range(4):
            for _ in range(4):
                for _ in range(4):
                    for _ in range(4):
                        t = self.face

                        # 上の面と前の面が一致しているとき
                        if t[0] == s[0] and t[1] == s[1]:

                            # returnを使うことでbreakが必要なくなる
                            return self.face[2]

                        self.face = [t[1], t[5], t[2], t[3], t[0], t[4]]
                    self.face = [t[4], t[0], t[2], t[3], t[5], t[1]]
                self.face = [t[3], t[1], t[0], t[5], t[4], t[2]]
            self.face = [t[2], t[1], t[5], t[0], t[4], t[3]]


# インスタンスaのfaceに出目のlistを割り当てる
a = dice(list(map(int, input().split())))

q = int(input())

for i in range(q):
    s = [0, 0]
    s[0], s[1] = map(int, input().split())

    # 戻り値である右側面が出力
    print(a.searchFace(s))

