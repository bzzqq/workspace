def quick_sort(alist, start, end):
    if start >= end:  # 递归的退出条件
        return
    mid = alist[start]  # 设定起始的基准元素
    low = start  # low为序列左边在开始位置的由左向右移动的游标
    high = end  # high为序列右边末尾位置的由右向左移动的游标
    while low < high:
        # 如果low与high未重合，high(右边)指向的元素大于等于基准元素，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]
    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
    alist[low] = mid  # 将基准元素放到该位置,
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low - 1)  # start :0  low -1 原基准元素靠左边一位
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, end)  # low+1 : 原基准元素靠右一位  end: 最后


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)
