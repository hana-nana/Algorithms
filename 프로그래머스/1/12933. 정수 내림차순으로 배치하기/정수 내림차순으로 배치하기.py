def solution(n):
    temp = str(n)
    answer = sorted(temp, reverse=True)
    return int("".join(answer))