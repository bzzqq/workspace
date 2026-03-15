def line(n):
    # dp[n] = [1] * n
    dp = [1 * n for _ in range(n+1)]
    return dp
print(line(5))
    # if n >= 2:
    #     line(n) = [1] * n
    #     for i in range(1, n - 1)
    #     line(n)[i] = line(n - 1)[i - 1] + line(n - 1)[i]