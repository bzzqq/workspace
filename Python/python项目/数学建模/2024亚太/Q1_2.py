import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler

# 创建数据集
data = pd.DataFrame({
    "Year": [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
    "Urbanization": [62.71, 63.89, 64.72, 65.22, 66.16, 67.68, 68.87, 70.05],
    "Per_Capita_Income": [21559, 21210, 24100, 24538, 26796, 28602, 30524, 32573],
    "Aging_Ratio": [12.6, 13.5, 14.2, 14.9, 15.4, 15.9, 16.4, 16.9],
    "Single_Ratio": [16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5],
    "Cat_Count": [4412, 4862, 5806, 6536, 6980, None, None, None],
    "Dog_Count": [5503, 5222, 5429, 5119, 5175, None, None, None]
})

# 填充缺失值
data.fillna(method='ffill', inplace=True)

# 确定自变量和因变量
features = ["Urbanization", "Per_Capita_Income", "Aging_Ratio", "Single_Ratio"]

# 训练集（2019-2022）和测试集（2023）
train_X = data[data["Year"] <= 2022][features]
test_X = data[data["Year"] == 2023][features]
future_X = data[data["Year"] >= 2024][features]

# 特征缩放
scaler = MinMaxScaler()
train_X_scaled = scaler.fit_transform(train_X)
test_X_scaled = scaler.transform(test_X)
future_X_scaled = scaler.transform(future_X)


# 训练并预测函数
def train_predict(X_train, y_train, X_test, X_future, animal_name, y_test_value):
    random_forest = RandomForestRegressor(random_state=42, n_estimators=100)
    random_forest.fit(X_train, y_train)
    pred = random_forest.predict(X_test)[0]
    future_pred = random_forest.predict(X_future)
    accuracy = 1 - abs(y_test_value - pred) / y_test_value if y_test_value else 0
    return pred, accuracy, future_pred


# 存储预测结果和准确率
predictions = {}
accuracies = {}
future_predictions = {}

for animal in ["Cat", "Dog"]:
    train_y = data[data["Year"] <= 2022][f"{animal}_Count"].astype(float)
    test_y_value = data[data["Year"] == 2023][f"{animal}_Count"].values[0]
    predictions[animal] = {}
    accuracies[animal] = {}
    future_predictions[animal] = {}
    pred, accuracy, future_pred = train_predict(train_X_scaled, train_y, test_X_scaled, future_X_scaled, animal, test_y_value)
    predictions[animal]["Random Forest"] = pred
    accuracies[animal]["Random Forest"] = accuracy
    future_predictions[animal]["Random Forest"] = future_pred

# 输出预测结果和准确率
print("Predictions and Accuracies for Cats and Dogs using Random Forest:")
for animal in ["Cat", "Dog"]:
    print(f"{animal} Results:")
    print(f"  Random Forest Prediction: {predictions[animal]['Random Forest']:.2f}, "
          f"Accuracy: {accuracies[animal]['Random Forest']:.2%}")

print("\nFuture Predictions for Cats and Dogs (2024-2026) using Random Forest:")
for animal in ["Cat", "Dog"]:
    print(f"{animal} Future Predictions:")
    future_preds = future_predictions[animal]["Random Forest"]
    print(f"  Random Forest: {', '.join(f'{pred:.2f}' for pred in future_preds)}")
