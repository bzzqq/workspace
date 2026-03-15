k = int(input("请输入k："))
n = 10000
while n <= 30000:
    sub1 = n // 100
    sub2 = n // 10 % 1000
    sub3 = n % 1000
    if sub1 % k == 0 and sub2 % k == 0 and sub3 % k == 0:
        print(n)
        n = n + 1
    else:
        n = n + 1
