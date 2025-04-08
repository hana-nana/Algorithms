def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) > 0:
        return sorted(answer)
    else:
        answer.append(-1)
        return answer