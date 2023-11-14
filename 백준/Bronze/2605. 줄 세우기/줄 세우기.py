std = int(input())
forward_lst = list(map(int, input().split()))
original_lst = list(range(1, std+1))

for i in range(std):
    forward, current = forward_lst[i], original_lst[i]
    for j in range(i, i-forward, -1):
        original_lst[j] = original_lst[j-1]
    original_lst[i-forward] = current
print(*original_lst)