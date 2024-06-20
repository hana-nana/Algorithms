def solution(my_string, is_suffix):
    n = len(is_suffix)
    m = len(my_string)
    if my_string[m-n:] == is_suffix:
        return 1
    else:
        return 0