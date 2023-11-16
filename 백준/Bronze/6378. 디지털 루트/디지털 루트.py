while True:
    N = input()
    if N == '0':
        break
    while True:
        if len(N) <= 1:
            break
        ans = 0
        for i in range(len(N)):
            ans += int(N[i])
        N = str(ans)
    print(N)

# while True:
#     N = int(input())
#     if N == 0:
#         break
#     ans = N
#     while ans >= 10:
#         tmp = 0
#         while ans > 0:
#             tmp += ans % 10
#             ans //= 10
#         ans = tmp
#     print(ans)