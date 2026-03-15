def binary_search(lis, left, right, num):
    if left > right:  # 递归结束条件
        return -1
    mid = (left + right) // 2 # 整除
    if num < lis[mid]:
        right = mid - 1
    elif num > lis[mid]:
        left = mid + 1
    else:
        return mid
    return binary_search(lis, left, right, num)


# 这里之所以会有return是因为必须要接收值,不然返回None
# 回溯到最后一层的时候,如果没有return,那么将会返回None
lis = [11, 32, 51, 21, 42, 9, 5, 6, 7, 8]
print(lis)
lis.sort()
print(lis)
while 1:
    num = int(input('输入要查找的数:'))
    res = binary_search(lis, 0, len(lis) - 1, num)
    print(res)
    if res == -1:
        print('未找到！')
    else:
        print('找到！')
