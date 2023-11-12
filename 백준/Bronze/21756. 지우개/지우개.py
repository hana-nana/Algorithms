N = int(input())
arr = []
for i in range(1, N+1):
    arr.append(i)

while len(arr) > 1:
    del arr[::2]

print(*arr)