import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import numpy as np

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

# 确定自变量和因变量
features = ["Urbanization", "Per_Capita_Income", "Aging_Ratio", "Single_Ratio"]

# 训练集（2019-2022）和测试集（2023）
train_X = data[data["Year"] <= 2022][features]
test_X = data[data["Year"] == 2023][features]
future_X = data[data["Year"] >= 2024][features]

train_y_cats = data[data["Year"] <= 2022]["Cat_Count"]
train_y_dogs = data[data["Year"] <= 2022]["Dog_Count"]
test_y_cats = data[data["Year"] == 2023]["Cat_Count"].values[0]
test_y_dogs = data[data["Year"] == 2023]["Dog_Count"].values[0]

# 初始化随机森林模型
random_forest = RandomForestRegressor(random_state=42, n_estimators=100)

# 存储预测结果和准确率
predictions = {"Cat": {}, "Dog": {}}
accuracies = {"Cat": {}, "Dog": {}}
future_predictions = {"Cat": {}, "Dog": {}}

# 训练并预测猫数量
random_forest.fit(train_X, train_y_cats)
pred_cats = random_forest.predict(test_X)[0]
predictions["Cat"]["Random Forest"] = pred_cats
accuracies["Cat"]["Random Forest"] = 1 - abs(test_y_cats - pred_cats) / test_y_cats

# 预测未来三年猫数量
future_predictions["Cat"]["Random Forest"] = random_forest.predict(future_X)

# 训练并预测狗数量
random_forest.fit(train_X, train_y_dogs)
pred_dogs = random_forest.predict(test_X)[0]
predictions["Dog"]["Random Forest"] = pred_dogs
accuracies["Dog"]["Random Forest"] = 1 - abs(test_y_dogs - pred_dogs) / test_y_dogs

# 预测未来三年狗数量
future_predictions["Dog"]["Random Forest"] = random_forest.predict(future_X)

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
