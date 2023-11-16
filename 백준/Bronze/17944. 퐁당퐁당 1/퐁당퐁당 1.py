N, T = map(int, input().split())

max_arms = 2 * N
# 팔을 드는 순서가 증가하다가 감소하는 전체 패턴의 길이
# 팔의 개수가 1에서 2 * N까지 증가하는 데 2 * N - 1 차례가 필요, 다시 1로 감소하는 데 2 * N - 1 필요
cycle_length = 4 * N - 2
# current는 주어진 차례 T를 전체 패턴 길이인 cycle_length로 나눈 나머지
current = T % cycle_length

# 만약 T가 cycle_length의 배수라면, current는 0
# 즉, 주어진 차례가 패턴의 마지막 차례인 경우를 처리하는 if문
# 이때, current를 cycle_length와 같게 설정해서, 패턴 마지막 차례에서 들어야 하는 팔 수 계산
if current == 0:
    current = cycle_length

# 바로 그 차례에 들어야 하는 팔의 개수(팔의 개수가 증가하는 단계)
if current <= max_arms:
    res = current
# 팔의 개수가 감소하는 단계
else:
    res = 2 * max_arms - current

print(res)
