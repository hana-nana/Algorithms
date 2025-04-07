def solution(s):
    temp_s = s.upper()
    pnum = 0
    ynum = 0
    for i in temp_s:
        if i == 'P':
            pnum += 1
        elif i == 'Y':
            ynum += 1
    if pnum == ynum:
        return True
    elif pnum + ynum == 0:
        return True
    return False