belt_cnt = int(input())

direction2 = 0
rotation_num = 1

for _ in range(belt_cnt):
    wheel1, wheel2, direction = map(int, input().split())
    if direction == 1:
        direction2 = (direction2 + 1) % 2
    rotation_num *= wheel2 / wheel1

print(direction2, int(rotation_num))
