k = int(input("请输入k："))
for value in range(10000, 30001):
    sub1 = value // 100
    sub2 = value // 10 % 1000
    sub3 = value % 1000
    if sub1 % k == 0 and sub2 % k == 0 and sub3 % k == 0:
        print(value)
