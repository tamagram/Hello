# classを使う
class dice:
    def __init__(self, face):
        self.face = face

    # selfを基準にほかのインスタンスと比較する
    def comparisonFace(self, other):

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

                        # selfの面と比較対象の面が一致しているか
                        if self.face == other.face:

                            # returnを使うことでbreakが必要なくなる
                            return "Yes"

                        self.face = [t[1], t[5], t[2], t[3], t[0], t[4]]
                    self.face = [t[4], t[0], t[2], t[3], t[5], t[1]]
                self.face = [t[3], t[1], t[0], t[5], t[4], t[2]]
            self.face = [t[2], t[1], t[5], t[0], t[4], t[3]]

        return "No"


# 組み合わせ比較処理
def comparisonDices(dices):
    # nC2であり 0 <= j < n , j < i < n
    for j in range(n - 1):

        # 樹形図だとわかりやすいがjの値が大きくなるほど組み合わせる回数が減っていく
        for i in range((n - 1) - j):
            if dices[j].comparisonFace(dices[(j + 1) + i]) == "Yes":

                return 0


dices = []
n = int(input())

for i in range(n):
    # インスタンスごとのfaceに出目のlistを割り当てる
    dices.append(dice(list(map(int, input().split()))))

# 一つでも一致するものがあればNoそうでなければYes
print("No") if comparisonDices(dices) == 0 else print("Yes")
