# lis = [1, 3, 4, 6, 7, 8, 10, 13, 14, 20, 22, 24, 30, 50, 80, 98, 100]
lis = list(range(100000000))
n = int(input('输入要查找的数:'))
left = 0
right = len(lis) - 1
while left <= right:
    mid = (left + right) // 2  # 整除
    if n > lis[mid]:
        left = mid + 1
    elif n < lis[mid]:
        right = mid - 1
    else:
        print("要查找的数在数组中的索引为%s" % mid)
        break
else:
    print("没有这个数据")
