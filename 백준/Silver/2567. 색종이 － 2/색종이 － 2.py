# arr[] -> 1로 색종이를 표시한
# 전체 순회한다
# 1을 만나면 4방향 0의 개수 -> 둘레
# 0에서 1로 바뀌는 부분, 1에서 0으로 바뀌는 부분 -> 둘레
# 전치행렬

# 행 우선순회 (함수화 가능)
# cnt = 0
# for lst(1차원) in arr(2차원):
#     for i in range(1, len(lst)):
#         # 리스트 요소를 반복하면서, 바로 직전에 있는거랑 내가 다르면
#         if lst[i-1] != lst[i]:
#             cnt += 1
# return cnt

def count(arr):
    cnt = 0
    for lst in arr:
        for i in range(1, len(lst)):
            if lst[i-1] != lst[i]:
                cnt += 1
    return cnt

N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())

    # 색종이 색칠
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

# 전치행렬 :
# 튜플로 묶이므로, 리스트로 변경원할 시 list(map(list, zip(*arr)))
arr_t = list(zip(*arr))
ans = count(arr) + count(arr_t)
print(ans)


