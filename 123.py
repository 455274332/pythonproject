def f(n, x, N):
    b = [0 for i in range(N)]
    i = 0
    while True:
        s = n // x  # 商
        y = n % x  # 余数
        b[i] = y
        i += 1
        if s == 0:
            break
        n = s
    # b.reverse()
    return bfee

print(f(8, 4, 2))

'''V2[ss3][screen] += V1[self.list_to_int(ss3_to_S[:-num_add], self.S)][screen] \ + sum([self.h[i] for i in ss3_to_S[-num_add:]])'''