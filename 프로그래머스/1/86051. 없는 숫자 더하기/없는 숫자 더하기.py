def solution(numbers):
    answer = 0
    for n in numbers:
        answer += n
    if answer != 45:
        return 45-answer
    return 0