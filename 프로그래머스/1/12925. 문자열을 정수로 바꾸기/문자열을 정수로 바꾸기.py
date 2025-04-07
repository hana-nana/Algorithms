def solution(s):
    if 1 <= len(s) <= 5:
        first = s[0]
        if first.isdigit():
            return int(s)
        else:
            if first == '+':
                return int(s[1:])
            else:
                return -1 * int(s[1:])

# <다른 풀이>
# def solution(s):
#     if 1 <= len(s) <= 5:
#         temp_list = []
#         for i in s:
#             temp_list.append(i)
#         answer = "".join(temp_list)
#     return int(answer)