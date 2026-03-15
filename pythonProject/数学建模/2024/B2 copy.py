import itertools
# 定义参数
p1 = [0.1, 0.2, 0.1, 0.2, 0.1, 0.05]  # 零配件 1 次品率
p2 = [0.1, 0.2, 0.1, 0.2, 0.2, 0.05]  # 零配件 2 次品率
p3 = [0.1, 0.2, 0.1, 0.2, 0.1, 0.05]  # 成品次品率
# p_f = np.array(p1) + np.array(p2) - np.multiply(p1, p2)  # 成品次品率
c1 = 4  # 零配件 1 购买单价
c2 = 18  # 零配件 2 购买单价
c_d1 = [2, 2, 2, 1, 8, 2]  # 检测零配件 1 成本
c_d2 = [3, 3, 3, 1, 1, 3]  # 检测零配件 2 成本
c_f = 6  # 成品装配成本
c_df = [3, 3, 3, 2, 2, 3]  # 成品检测成本
c_r = [6, 6, 30, 30, 10, 10]  # 调换损失
c_s = [5, 5, 5, 5, 5, 40]  # 拆解费用
n = 1000  # 假设生产 1000 件产品


# 计算总利润的函数
def calculate_total_profit(x1, x2, y, z, n):
    # 零配件检测成本
    C_1_detect = x1 * (n * c_d1)
    C_2_detect = x2 * (n * c_d2)
    # 成品检测成本
    C_f_detect = y * (n * (1 - p_f0) * c_df)
    # 装配成本
    C_f_assembly = n_t * c_f
    # 不合格成品的拆解成本
    C_disassemble = z * (n_f * (c_s - c1 - c2))
    # 调换损失
    C_replace = n_f * c_r
    # 计算总利润
    total_profit = 56 * n_t - n * (c1 + c2) - C_1_detect - C_2_detect - C_f_detect - C_disassemble - C_replace - C_f_assembly
    return total_profit


for i in range(0, 1):
    best_decision = None
    max_profit = float('-inf')
    p1 = p1[i]  # 零配件 1 次品率
    p2 = p2[i]  # 零配件 2 次品率
    p3 = p3[i]  # 成品次品率
    c_d1 = c_d1[i]  # 检测零配件 1 成本
    c_d2 = c_d2[i]  # 检测零配件 2 成本
    c_df = c_df[i]  # 成品检测成本
    c_r = c_r[i]  # 调换损失
    c_s = c_s[i]  # 拆解费用
    # 枚举所有可能的决策组合 (x1, x2, y, z)
    for decision in itertools.product([0, 1], repeat=4):
        x1, x2, y, z = decision
        # p_f0 = (1 - x1) * p1 + (1 - x2) * p2 - (1 - x1) * p1 * (1 - x2) * p2  # 零件次品率
        p_f0 = x1 * p1 + x2 * p2 - x1 * p1 * x2 * p2  # 零件次品率
        p_f = (1 - p_f0) * p3  # 成品次品率
        n_f = n * (1 - p_f0) * (1 - y) * p3  # 不合格成品量
        n_t = n * (1 - p_f0) - n * (1 - p_f0) * y * p3  # 成品总量
        p_f2 = (1 - x1) * p1 + (1 - x2) * p2 - (1 - x1) * p1 * (1 - x2) * p2 + (1 - ((1 - x1) * p1 + (1 - x2) * p2 - (1 - x1) * p1 * (1 - x2) * p2)) * p3 * (1 - y)  # 总次品率
        total_profit = calculate_total_profit(x1, x2, y, z, n)
        if total_profit > max_profit:
            max_profit = total_profit
            best_decision = decision
    # 输出结果
    x1, x2, y, z = best_decision
    print(f"情况{i + 1}：\n"
          f"最佳决策方案为：\n"
          f"检测零配件 1：{'是' if x1 == 1 else '否'}\n"
          f"检测零配件 2：{'是' if x2 == 1 else '否'}\n"
          f"检测成品：{'是' if y == 1 else '否'}\n"
          f"拆解不合格成品：{'是' if z == 1 else '否'}\n"
          f"总利润为：{max_profit}")
