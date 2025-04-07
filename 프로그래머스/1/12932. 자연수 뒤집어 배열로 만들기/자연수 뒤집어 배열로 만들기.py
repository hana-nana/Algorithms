def solution(n):
    answer = []
    n_list = list(str(n))
    while n_list:
        p = n_list.pop()
        answer.append(int(p))
    return answer