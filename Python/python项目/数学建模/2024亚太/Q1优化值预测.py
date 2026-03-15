import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, KFold

# 一、数据准备

# 创建数据字典
data = {
    '年份': [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
    '中国城市化率': ['62.71%', '63.89%', '64.72%', '65.22%', '66.16%', '67.68%', '68.87%', '70.05%'],
    '中国居民人均消费支出(元)': [21559, 21210, 24100, 24538, 26796, 28602, 30524, 32573],
    '老龄化比例%（65+）': [12.6, 13.5, 14.2, 14.9, 15.4, 15.9, 16.4, 16.9],
    '单身人口比例%': [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5],
    '猫数量(万只)': [4412, 4862, 5806, 6536, 6980, 7499, 7983, 8491],
    '狗数量(万只)': [5503, 5222, 5429, 5119, 5175, 5205, 5205, 5205],
    '宠物食品': [336, 401, 452, 486, 570, np.nan, np.nan, np.nan],
    '宠物医疗': [483, 655, 881, 1216, 1726, np.nan, np.nan, np.nan],
    '宠物服务': [298, 368, 470, 581, 714, np.nan, np.nan, np.nan],
    '宠物总体消费': [2005, 2058, 2489, 3117, 3924, np.nan, np.nan, np.nan]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 数据预处理
# 将百分比字符串转换为小数
df['中国城市化率'] = df['中国城市化率'].str.rstrip('%').astype(float) / 100
df['老龄化比例%（65+）'] = df['老龄化比例%（65+）'] / 100
df['单身人口比例%'] = df['单身人口比例%'] / 100

# 二、特征和目标变量

# 自变量列表（进行特征选择，剔除多重共线性强的特征）
features = ['中国居民人均消费支出(元)', '猫数量(万只)', '狗数量(万只)']

# 因变量列表
targets = ['宠物食品', '宠物医疗', '宠物服务', '宠物总体消费']

# 分割训练集和测试集（2019-2022为训练集，2023为测试集）
train_df = df[df['年份'] <= 2022].dropna(subset=targets)
test_df = df[df['年份'] == 2023]
future_df = df[df['年份'] >= 2024]

# 三、模型训练和预测

# 标准化特征
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(train_df[features])
X_test_scaled = scaler.transform(test_df[features])
X_future_scaled = scaler.transform(future_df[features])

# 设置岭回归的正则化强度参数
alpha = 1.0  # 可以调整alpha值，alpha越大正则化力度越强

# 创建结果存储字典
results = {}

for target in targets:
    # 1. 准备数据
    y_train = train_df[target].values
    y_test = test_df[target].values
    X_train = X_train_scaled
    X_test = X_test_scaled
    X_future = X_future_scaled

    # 2. 模型训练（使用岭回归）
    model = Ridge(alpha=alpha)
    model.fit(X_train, y_train)

    # 3. 交叉验证评估模型
    kf = KFold(n_splits=3, shuffle=True, random_state=42)
    scores = cross_val_score(model, X_train, y_train, cv=kf, scoring='neg_mean_absolute_percentage_error')
    mean_score = -scores.mean() * 100  # 转换为正的百分比误差

    # 4. 模型预测
    y_pred = model.predict(X_test)
    y_future = model.predict(X_future)

    # 5. 计算误差率
    error_rate = abs(y_pred[0] - y_test[0]) / y_test[0] * 100

    # 6. 确保预测值递增（未来年份）
    y_future_corrected = []
    last_value = y_test[0]
    for yf in y_future:
        yf = max(yf, last_value)  # 确保预测值不小于上一年
        y_future_corrected.append(yf)
        last_value = yf

    # 7. 存储结果
    results[target] = {
        '2023实际值': y_test[0],
        '2023预测值': y_pred[0],
        '误差率(%)': error_rate,
        '交叉验证平均误差率(%)': mean_score,
        '2024-2026预测值': y_future_corrected
    }

# 四、结果展示

for target in targets:
    res = results[target]
    print(f"--- {target} ---")
    print(f"2023实际值: {res['2023实际值']:.2f}")
    print(f"2023预测值: {res['2023预测值']:.2f}")
    print(f"误差率: {res['误差率(%)']:.2f}%")
    print(f"交叉验证平均误差率: {res['交叉验证平均误差率(%)']:.2f}%")
    print("2024-2026预测值:")
    for year, value in zip(future_df['年份'], res['2024-2026预测值']):
        print(f"{year}年预测值: {value:.2f}")
    print("\n")
