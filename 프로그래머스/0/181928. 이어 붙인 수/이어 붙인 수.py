def solution(num_list):
    n = []
    m = []
    for i in num_list:
        if i % 2 == 0:
            n.append(i)
        else:
            m.append(i)
    n_str = ''.join(map(str, n))
    n_int = int(n_str)
    m_str = ''.join(map(str, m))
    m_int = int(m_str)
    return n_int + m_int