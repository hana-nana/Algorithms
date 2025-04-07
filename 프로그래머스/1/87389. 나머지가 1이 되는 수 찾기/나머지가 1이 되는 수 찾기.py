def solution(n):
    answer = []
    x = 1
    while x <= n:
        if n % x == 1:
            answer.append(x)
        x += 1
    return min(answer)