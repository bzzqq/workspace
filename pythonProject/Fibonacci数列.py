n = int(input("请输入n："))


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("fibonacci(", n, ")=", fibonacci(n))
