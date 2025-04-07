def solution(x, n):
    answer = [x]
    inum = x
    while len(answer) < n:
        inum += x
        answer.append(inum)
    return answer