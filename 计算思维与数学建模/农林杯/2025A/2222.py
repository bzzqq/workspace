import pulp
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD


def prepare_data():
    """准备数据，单位统一为吨"""
    destinations = ["石家庄", "唐山", "秦皇岛", "邯郸", "邢台", "保定", "张家口", "承德", "沧州", "廊坊", "衡水", "北京", "天津"]

    # 各目标地需求（万吨转换为吨）
    demand_10k_tons = [
        31.538220487736385, 30.175433907507962, 9.065830953941212, 36.97771906010111, 36.911715151657, 43.38398076202959, 38.16967199494477, 14.959591719715412, 39.91295169443925, 20.309790886538106, 30.38509338138926, 10.53, 6.34
    ]
    demand = {d: q * 10000 for d, q in zip(destinations, demand_10k_tons)}

    # 仓库库存（万吨转换为吨）
    warehouses = ["仓库A", "仓库B", "仓库C"]
    stock_10k_tons = [85, 120, 105]
    stock = {w: q * 10000 for w, q in zip(warehouses, stock_10k_tons)}

    # 距离矩阵（公里）
    distance_matrix = [[410.2, 63.7, 177.6, 562.2, 516.3, 275.4, 312.3, 162, 246, 138, 376, 135.9, 123.2], [80.8, 385.3, 530.2, 213.2, 167.3, 149.6, 439.1, 513.4, 168.2, 272.9, 70.6, 292, 271.7],
                       [124.4, 428.6, 573.6, 150.3, 104.4, 222.5, 518.8, 556.5, 211.5, 315.9, 55, 335.1, 315.1]]
    distances = {(w, d): distance_matrix[i][j] for i, w in enumerate(warehouses) for j, d in enumerate(destinations)}

    # 车型参数（仅需单位运输成本）
    vehicle_types = ["小型车", "中型车", "重型车"]
    vehicle_info = {"小型车": {"capacity": 10, "cost": 0.145}, "中型车": {"capacity": 20, "cost": 0.0975}, "重型车": {"capacity": 40, "cost": 0.045}}

    return {"destinations": destinations, "warehouses": warehouses, "demand": demand, "stock": stock, "distances": distances, "vehicle_types": vehicle_types, "vehicle_info": vehicle_info}


def build_model(data):
    """构建优化模型"""
    prob = LpProblem("FertilizerDistribution_Problem2", LpMinimize)

    # 决策变量：x[车型][仓库][目标地] = 车次数（整数）
    x = LpVariable.dicts("x", [(v, w, d) for v in data["vehicle_types"] for w in data["warehouses"] for d in data["destinations"]], lowBound=0, cat="Integer")

    # ---------------------- 目标函数 ----------------------
    # 总运输成本 = sum(车次数 * 距离 * 车型单位成本 * 车型容量)
    total_cost = lpSum(x[v, w, d] * data["distances"][(w, d)] * data["vehicle_info"][v]["cost"] * data["vehicle_info"][v]["capacity"] for v in data["vehicle_types"] for w in data["warehouses"] for d in data["destinations"])

    # 总车次数 = sum(车次数)
    total_trips = lpSum(x[v, w, d] for v in data["vehicle_types"] for w in data["warehouses"] for d in data["destinations"])

    # 多目标加权（权重需调整量级）
    prob += total_cost + 0.001 * total_trips  # 1元成本 ≈ 1000次车次

    # ---------------------- 约束条件 ----------------------
    # 1. 各仓库发货量不超过库存
    for w in data["warehouses"]:
        prob += lpSum(x[v, w, d] * data["vehicle_info"][v]["capacity"] for v in data["vehicle_types"] for d in data["destinations"]) <= data["stock"][w], f"Stock_Constraint_{w}"

    # 2. 各目标地收货量不超过需求（若需至少满足90%需求，改为 >= 0.9*demand[d]）
    for d in data["destinations"]:
        prob += lpSum(x[v, w, d] * data["vehicle_info"][v]["capacity"] for v in data["vehicle_types"] for w in data["warehouses"]) <= data["demand"][d], f"Demand_Constraint_{d}"

    # 3. 总发货量等于总库存（强制发完库存）
    total_stock = sum(data["stock"].values())
    prob += lpSum(x[v, w, d] * data["vehicle_info"][v]["capacity"] for v in data["vehicle_types"] for w in data["warehouses"] for d in data["destinations"]) == total_stock, "Total_Stock_Constraint"

    return prob, x, total_cost, total_trips  # 返回总运输成本和总车次数


def solve_model(prob):
    """求解模型"""
    solver = PULP_CBC_CMD(msg=False)
    prob.solve(solver)

    if pulp.LpStatus[prob.status] != "Optimal":
        raise RuntimeError(f"模型求解失败，状态：{pulp.LpStatus[prob.status]}")

    return prob


def extract_results(prob, data, x, total_cost, total_trips):
    """提取结果"""
    total_cost_value = pulp.value(total_cost)
    total_trips_value = pulp.value(total_trips)

    # 计算供给率
    total_demand = sum(data["demand"].values())
    total_supply = sum(data["stock"].values())
    average_supply_rate = total_supply / total_demand

    # 提取运输计划详情
    transport_details = {}
    for w in data["warehouses"]:
        transport_details[w] = {}
        for d in data["destinations"]:
            transport_details[w][d] = {}
            total_quantity = 0
            for v in data["vehicle_types"]:
                trips = x[v, w, d].varValue
                if trips > 0:
                    quantity = trips * data["vehicle_info"][v]["capacity"]
                    transport_details[w][d][v] = {"trips": trips, "quantity": quantity}
                    total_quantity += quantity
            if total_quantity > 0:
                transport_details[w][d]["total"] = total_quantity

    return {"total_cost": total_cost_value, "total_trips": total_trips_value, "average_supply_rate": average_supply_rate, "details": transport_details}


def print_results(results, data):
    """打印结果"""
    print(f"\n{'=' * 40}")
    print(f"{'优化结果':^40}")
    print(f"{'=' * 40}")
    print(f"总运输成本: {results['total_cost']:,.2f} 元")
    print(f"总运输车次: {results['total_trips']:.0f} 次")
    print(f"平均供给率: {results['average_supply_rate']:.2%}\n")

    print(f"{'详细运输计划':^40}")
    for w in data["warehouses"]:
        print(f"\n仓库: {w}")
        warehouse_total = 0
        for d in data["destinations"]:
            if not results['details'][w][d]:
                continue
            total = results['details'][w][d].get("total", 0)
            if total == 0:
                continue
            warehouse_total += total
            print(f"  → 目标地: {d}")
            for v in data["vehicle_types"]:
                if v in results['details'][w][d]:
                    detail = results['details'][w][d][v]
                    print(f"    车型: {v:<5} 车次: {detail['trips']:3.0f} 次  运量: {detail['quantity'] / 10000:6.2f} 万吨")
            print(f"    总运量: {total / 10000:6.2f} 万吨")
        print(f"仓库 {w} 总发货量: {warehouse_total / 10000:6.2f} 万吨")


if __name__ == "__main__":
    # 数据准备
    data = prepare_data()

    # 模型构建
    prob, x, total_cost, total_trips = build_model(data)

    # 模型求解
    prob = solve_model(prob)

    # 结果提取
    results = extract_results(prob, data, x, total_cost, total_trips)

    # 结果打印
    print_results(results, data)
