goods = [4, 10, 7, 11, 3, 5, 14, 2]
max_w = 7
m = {(i, w): 0 for i in range(len(goods)) for w in range(max_w + 1)}
ship = []
for i in range(1, len(goods)):
    for w in range(1, max_w + 1):
        if goods[i] > w:
            # 装不下第i个宝物，即不装第i个宝物
            m[(i, w)] = m[(i - 1, w)]            
        else:
            # 装得下第i个宝物时，在不装第i个宝物与装第i个宝物这两种情况下，取最大价值
            m[(i, w)] = max(m[(i - 1, w)],
                            m[(i - 1, w - goods[i])] + goods[i])
# 输出结果
print(m[(len(goods) - 1, max_w)])
