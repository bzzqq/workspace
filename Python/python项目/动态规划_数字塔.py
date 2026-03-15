# import random

# def generating_tower(n):
#     """随机生成数塔数"""
#     x = []
#     y = []
#     for i in range(n):
#         for j in range(i + 1):
#             x.append(random.randint(0,9))
#         y.append(x)
#         x = []
#     return y
# print(generating_tower(3))

n = 5
y = [[9], [12, 15], [10, 6, 8], [2, 18, 9, 5], [19, 7, 10, 4, 16]]

# for d in range(n - 1, -1, -1):
#     for f in range(d + 1):
#         print((d, f), '=', (y[d][f]), end='-------')
#     print()
# (3, 0) = 7-------(3, 1) = 2-------(3, 2) = 9-------(3, 3) = 5-------
# (2, 0) = 3-------(2, 1) = 6-------(2, 2) = 9-------
# (1, 0) = 8-------(1, 1) = 4-------
# (0, 0) = 5-------

# print(y)
# [[5], [8, 4], [3, 6, 9], [7, 2, 9, 5]]

# 父子相加取大者
for a in range(n - 2, -1, -1):
    for b in range(a + 1):
        y[a][b] = max((y[a][b] + y[a + 1][b]), (y[a][b] + y[a + 1][b + 1]))
        print((a, b), '=', (y[a][b]), end='-------')
    print()
# (2, 0) = 10-------(2, 1) = 15-------(2, 2) = 18-------
# (1, 0) = 23-------(1, 1) = 22-------
# (0, 0) = 28-------

# print(y)
# [[28], [23, 22], [10, 15, 18], [7, 2, 9, 5]]

num1 = y[0][0]
print('最大值为:%d' % (num1))
print('经过的数字为:', end='')
m = 0
for k in range(1, n):
    m = y[k].index(max(y[k][m], y[k][m + 1]))
    num2 = y[k][m]
    print(num1 - num2, end='->')
    num1 = num2
    if k == n - 1:
        print(num1)
