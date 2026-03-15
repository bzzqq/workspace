
a = list(range(100000000))
n = float(input('输入要查找的数:'))
for i in a:
    if n == i:
        print("要查找的数在数组中的索引为%s" % i)
        break
else:
    print("没有这个数据")