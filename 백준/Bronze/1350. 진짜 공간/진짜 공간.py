file_num = int(input())
file_size = list(map(int, input().split()))
cle = int(input())

res = 0
for i in file_size:
    # 현재 확인하고 있는 값을 클러스터 크기로 나눈 나머지가 0보다 크면
    # 하나의 클러스터를 더 사용해야 하므로 몫에 1을 더해서 누적
    if i % cle > 0:
        res += (i // cle + 1)
    # 0 이하일 경우 하나 더 사용할 필요 없으므로 단순히 몫만 누적
    else:
        res += (i // cle)

print(cle * res)
