from collections import deque

d = deque()
n = int(input())
for _ in range(n):
    # commandは分割され格納される
    command = input().split()
    if command[0] == "insert":
        d.appendleft(command[1])
    # d←何か入っているとき真
    elif d and command[0] == "deleteFirst":
        d.popleft()
    elif d and command[0] == "deleteLast":
        d.pop()
    elif command[1] in d and command[0] == "delete":
        d.remove(command[1])

print(" ".join(map(str, d)))
