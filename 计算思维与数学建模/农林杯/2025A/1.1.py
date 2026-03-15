import numpy as np
from scipy.optimize import linprog

# 各仓库的化肥实际存量（万吨）
warehouse_stocks = np.array([85, 120, 105])

# 京津冀地区的化肥需求量（万吨）
city_demands = np.array(
    [31.538220487736385, 30.175433907507962, 9.065830953941212, 36.97771906010111, 36.911715151657, 43.38398076202959, 38.16967199494477, 14.959591719715412, 39.91295169443925, 20.309790886538106, 30.38509338138926, 10.53, 6.34])

# 各仓库与配送目标间的公路距离（公里）
distances = np.array([[410.2, 63.7, 177.6, 562.2, 516.3, 275.4, 312.3, 162.0, 246.0, 138.0, 376.0, 135.9, 123.2], [80.8, 385.3, 530.2, 213.2, 167.3, 149.6, 439.1, 513.4, 168.2, 272.9, 70.6, 292.0, 271.7],
                      [124.4, 428.6, 573.6, 150.3, 104.4, 222.5, 518.8, 556.5, 211.5, 315.9, 55.0, 335.1, 315.1]])

# 运输成本为0.10元/公里/吨
transport_cost = 0.10

# 构建目标函数系数，目标是最小化总运输成本
c = np.array([dist * transport_cost for sublist in distances for dist in sublist])

# 构建不等式约束矩阵 A_ub 和向量 b_ub（每个仓库发货量不超过库存）
A_ub = []
b_ub = []
num_cities = len(city_demands)
for i in range(len(warehouse_stocks)):
    row = [0] * num_cities * len(warehouse_stocks)
    for j in range(num_cities):
        row[i * num_cities + j] = 1
    A_ub.append(row)
    b_ub.append(warehouse_stocks[i])

# 构建不等式约束确保每个地区分配量不超过需求量
for j in range(num_cities):
    row = [0] * num_cities * len(warehouse_stocks)
    for i in range(len(warehouse_stocks)):
        row[i * num_cities + j] = 1
    A_ub.append(row)
    b_ub.append(city_demands[j])

# 构建等式约束矩阵 A_eq 和向量 b_eq（所有库存都要分配出去）
A_eq = []
b_eq = []
for i in range(len(warehouse_stocks)):
    row = [0] * num_cities * len(warehouse_stocks)
    for j in range(num_cities):
        row[i * num_cities + j] = 1
    A_eq.append(row)
b_eq = warehouse_stocks

# 求解线性规划问题
res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, method='highs', bounds=(0, None))

if res.status == 0:
    # 提取结果并输出
    optimal_solution = res.x.reshape(len(warehouse_stocks), len(city_demands))
    print('最优配送方案（万吨）：')
    print(optimal_solution)
    print('最小总运输成本（元）：', np.sum(optimal_solution * distances * transport_cost))

    # 计算各地区需求满足率
    demand_satisfaction = np.sum(optimal_solution, axis=0) / city_demands
    print('各地区需求满足率：', demand_satisfaction)
    print('平均需求满足率：', np.mean(demand_satisfaction))
else:
    print(f'线性规划求解失败，状态码: {res.status}')
    if res.status == 1:
        print('超过了迭代次数限制')
    elif res.status == 2:
        print('问题不可行')
    elif res.status == 3:
        print('目标函数无界')
    elif res.status == 4:
        print('算法特定的错误')
