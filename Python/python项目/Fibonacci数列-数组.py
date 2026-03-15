n = (input("请输入n："))
n = int(n)


def fib(n):
    dp = [0 for _ in range(n+1)]
    # 基础值，也就是baseline
    dp[1] = dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


print("fib(", n, ")=", fib(n))
