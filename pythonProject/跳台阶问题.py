n = int(input("请输入n："))


def f(n):
    if n <= 2:
        return n
    return f(n - 1) + f(n - 2)


print(f(n))
