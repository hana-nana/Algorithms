# 스위치 변경하는 함수
def change(num):
    if switch[num] == 0:
        switch[num] = 1
    elif switch[num] == 1:
        switch[num] = 0
    return

N = int(input())
# 인덱스가 0부터 시작하므로, 첫번째 값이 1이되도록 하기 위해 switch 리스트 앞에 -1 추가(0번째 인덱스는 안쓰기 위해)
switch = [-1]+list(map(int, input().split()))
std = int(input())
for _ in range(std):
    gender, num = map(int, input().split())

    # 남자일 경우
    if gender == 1:
        # 배수
        for i in range(num, N+1, num):
            change(i)

    # 여자일 경우
    elif gender == 2:
        # 먼저 자기 자신부터 바꿈
        change(num)
        # N 범위 절반씩 탐색하므로
        for d in range(N//2):
            # 스위치 범위를 넘어가면 멈춤
            if num+d > N or num-d < 1:
                break
            # 양 옆의 스위치가 같으면, 양 옆 모두 바꿔줌
            if switch[num+d] == switch[num-d]:
                change(num+d)
                change(num-d)
            # 자기자신의 양옆이 같지 않으면 멈춤
            else:
                break

# 한 줄에 20개씩 끊어서 출력
for i in range(1, N+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()