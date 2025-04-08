def solution(x):
    digit = [int(i) for i in str(x)]
    sum_num = 0
    for d in digit:
        sum_num += d
    if x % sum_num == 0:
        return True
    return False