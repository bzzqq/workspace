goods = [4, 10, 7, 11, 3, 5, 14, 2]
goods_sort = sorted(goods)  # 对重量排序
w = 7
m = 0
tmp = 0  # m记录装载古董数量, tmp记录装载古董重量
ship = []  # 记录装载的古董
for a in goods_sort:
    tmp = tmp + a
    if tmp <= w:
        m = m + 1
        ship.append(a)

print("装载古董的数量:", m)
print("装载的古董", ship)
