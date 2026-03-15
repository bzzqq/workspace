a = float(input("请输入a："))
x0 = float(input("请输入x0："))
x1 = 0.5 * (x0 + a / x0)
while abs(x1 - x0) > 0.000001:
    x0 = x1
    x1 = 0.5 * (x0 + a / x0)
    print(x1)
print(x1)
