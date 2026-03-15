n = int(input("请输入n："))


def fib(n):
    if n <= 2:
        return 1
    prev = 1
    curr = 1
    for i in range(3, n+1):
        # prev, curr = curr, prev + curr
        sum = prev + curr
        prev = curr
        curr = sum
    return curr


print("fib(", n, ")=", fib(n))
