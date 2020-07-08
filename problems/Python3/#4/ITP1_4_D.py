n = int(input())

# map関数の返す値は list 型ではなく iterator 型
# リストとして取得したい場合は list() 関数を使って変換する
a = list(map(int, input().split()))

print(min(a), max(a), sum(a))
