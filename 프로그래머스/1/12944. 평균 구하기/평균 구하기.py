def solution(arr):
    l = len(arr)
    temp = 0
    for i in arr:
        temp += i
    avg = temp/l
    return avg