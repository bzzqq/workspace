import random
import copy


def generate_num_tower(height):
    num_tower = []
    for i in range(height):
        # 每层的数字数量是当前层数 + 1
        layer = [random.randint(70, 99) for _ in range(i + 1)]
        num_tower.append(layer)
    return num_tower


# 生成一个20层的数塔
num_tower = generate_num_tower(20)
num_tower2 = copy.deepcopy(num_tower)

# 打印数塔
for layer in num_tower:
    print('  '.join(str(num) for num in layer).center(80))


def max_path_sum(num_tower):
    # 从倒数第二层开始向上计算
    for i in range(len(num_tower) - 2, -1, -1):
        for j in range(len(num_tower[i])):
            # 选择两个子节点中较大的一个加上当前节点的值
            num_tower[i][j] += max(num_tower[i + 1][j], num_tower[i + 1][j + 1])
    # 顶部的元素即为最大路径和
    return num_tower[0][0]


# 计算最大路径和
max_sum = max_path_sum(num_tower)
print("The maximum path sum is:", max_sum)

# 父子相加取大者
for a in range(len(num_tower2) - 2, -1, -1):
    for b in range(a + 1):
        num_tower2[a][b] = max((num_tower2[a][b] + num_tower2[a + 1][b]), (num_tower2[a][b] + num_tower2[a + 1][b + 1]))
        # print((a, b), '=', (num_tower2[a][b]), end='-------')
    # print()

num1 = num_tower2[0][0]
print('最大值为:%d' % (num1))
print('经过的数字为:', end='')
m = 0
for k in range(1, len(num_tower2)):
    m = num_tower2[k].index(max(num_tower2[k][m], num_tower2[k][m + 1]))
    num2 = num_tower2[k][m]
    print(num1 - num2, end='->')
    num1 = num2
    if k == len(num_tower2) - 1:
        print(num1)
