N = int(input())
candidate = list(map(int, input().split()))
main, sub = map(int, input().split())

cnt = 0
for i in range(len(candidate)):
    if candidate[i] - main <= 0:
        cnt += 1
    else:
        cnt += 1
        rest = candidate[i] - main
        if rest % sub == 0:
            cnt += (rest // sub)
        else:
            cnt += (rest // sub) +1

print(cnt)