goods = [
    None, {
        'w': 3,
        'v': 24
    }, {
        'w': 1,
        'v': 10
    }, {
        'w': 2,
        'v': 15
    }, {
        'w': 4,
        'v': 25
    }
]
# 设置背包最大承重
max_w = 5
# 初始化二维表格m[(i, w)]，将表格中所有价值均初始化为0
# 表示前i个宝物中，最大重量w的组合，所得到的最大价值
# 当i或w为0时，价值为0
m = {(i, w): 0 for i in range(len(goods)) for w in range(max_w + 1)}
# 逐个填写二维表格
# 外层循环为 i个宝物，[1,9)的循环
# 内层循环为 重量w，[1, max_w+1)的循环
for i in range(1, len(goods)):
    for w in range(1, max_w + 1):
        if goods[i]['w'] > w:
            # 装不下第i个宝物，即不装第i个宝物
            m[(i, w)] = m[(i - 1, w)]
        else:
            # 装得下第i个宝物时，在不装第i个宝物与装第i个宝物这两种情况下，取最大价值
            m[(i, w)] = max(m[(i - 1, w)],
                            m[(i - 1, w - goods[i]['w'])] + goods[i]['v'])
# 输出结果
print(m[(len(goods) - 1, max_w)])
print(m)