from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
# 数据输入
n = 8  # 零配件数量
m = 2  # 工序数量
# 零配件次品率
p = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# 购买单价、检测成本
c_b = [2, 8, 12, 2, 8, 12, 8, 12]  # 零配件的购买单价
c_d = [1, 1, 2, 1, 1, 2, 1, 2]  # 零配件的检测成本
# 装配成本、拆解费用
c_a = [8, 8]  # 每道工序的装配成本
c_s = 10  # 拆解费用
# 成品相关成本
market_price = 200  # 市场售价
loss_cost = 40  # 调换损失
# 成品最大容忍次品率
P_max = 0.1  # 成品最大次品率限制
# 建立优化模型
model = LpProblem("Production_Decision", LpMinimize)
# 决策变量
x = [LpVariable(f"x{i+1}", cat=LpBinary) for i in range(n)]  # 零配件检测决策变量
y = [LpVariable(f"y{j+1}", cat=LpBinary) for j in range(m)]  # 半成品检测决策变量
z = LpVariable("z", cat=LpBinary)  # 成品拆解决策变量
# 目标函数：最小化总成本
model += lpSum([x[i] * c_d[i] + (1 - x[i]) * p[i] * loss_cost + c_b[i] for i in range(n)]) \
 + lpSum([y[j] * c_a[j] for j in range(m)]) \
 + z * c_s
# 约束条件：成品的次品率不能超过最大容忍次品率
# 假设检测能完全发现并丢弃次品零件，简化后次品率约束
model += (1 - lpSum([(1 - p[i] * x[i]) for i in range(n)]) / n) <= P_max
# 求解模型
model.solve()
# 输出结果
print("Optimal Decision:")
for i in range(n):
    print(
        f"Component {i+1}: {'Inspect' if x[i].value() == 1 else 'Do not inspect'}"
    )
for j in range(m):
    print(
        f"Process {j+1} Half-product: {'Inspect' if y[j].value() == 1 else 'Do not inspect'}"
    )
print(
    f"Finished Product: {'Disassemble faulty products' if z.value() == 1 else 'Do not disassemble faulty products'}"
)
# 输出目标函数值
print(f"Total Minimum Cost: {model.objective.value()}")
