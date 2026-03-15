# 每个商品元组表示（价格，重量）
# goods = [(8, 4), (50, 10), (14, 7), (44, 11), (9, 3), (20, 5), (28, 14), (6, 2)]
# 对商品按单位价值进行排序
# goods.sort(key=lambda x: x[0] / x[1], reverse=True)
# print(goods)
goods = [(50, 10), (44, 11), (20, 5), (9, 3), (6, 2), (8, 4), (14, 7), (28, 14)]

w = 50
# w 表示背包的容量


def fractional_backpack(goods, w):
    # m 表示每个商品拿走多少个
    total_v = 0
    m = [0 for _ in range(len(goods))]
    for i, (price, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            total_v += price
            w -= weight
            # m[i] = 1 if w>= weight else weight / w
        else:
            m[i] = w / weight
            total_v += m[i] * price
            w = 0
            break
    return m, total_v


res1, res2 = fractional_backpack(goods, w)
print(res1, res2)
