def solution(n):
    if 0 <= n <= 3000:
        answer = 0
        temp = 1
        while temp <= n:
            if n % temp == 0:
                answer += temp
            temp += 1
    return answer