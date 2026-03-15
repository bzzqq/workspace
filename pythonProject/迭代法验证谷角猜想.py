n = int(input("请输入n："))
while n != 1:
    if n % 2 == 0:
        n = n / 2
        print(n)
    else:
        n = 3 * n + 1
        print(n)
print("猜想成功")
# print("共迭代" + str(k) + "次")
