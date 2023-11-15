T = int(input())
for tc in range(1, T+1):
    quiz = input()
    cnt = 0
    score = 0
    for i in quiz:
        if i == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)