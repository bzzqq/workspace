import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

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
train_X = data[data["Year"] <= 2022][features]
test_X = data[data["Year"] == 2023][features]
future_X = data[data["Year"] >= 2024][features]

train_y_cats = data[data["Year"] <= 2022]["Cat_Count"]
train_y_dogs = data[data["Year"] <= 2022]["Dog_Count"]
test_y_cats = data[data["Year"] == 2023]["Cat_Count"].values[0]
test_y_dogs = data[data["Year"] == 2023]["Dog_Count"].values[0]

# 初始化线性回归模型
linear_regression_model_cats = LinearRegression()
linear_regression_model_dogs = LinearRegression()

# 模型训练
linear_regression_model_cats.fit(train_X, train_y_cats)
linear_regression_model_dogs.fit(train_X, train_y_dogs)

# 对2023年的预测
pred_cats_2023 = linear_regression_model_cats.predict(test_X)[0]
pred_dogs_2023 = linear_regression_model_dogs.predict(test_X)[0]

# 计算2023年的准确率
accuracy_cats_2023 = 1 - abs(test_y_cats - pred_cats_2023) / test_y_cats
accuracy_dogs_2023 = 1 - abs(test_y_dogs - pred_dogs_2023) / test_y_dogs

# 对未来三年的预测
future_cats = linear_regression_model_cats.predict(future_X)
future_dogs = linear_regression_model_dogs.predict(future_X)

# 输出结果
print("2023 Predictions:")
print(f"  Cats - Predicted: {pred_cats_2023:.2f}, Actual: {test_y_cats}, Accuracy: {accuracy_cats_2023:.2%}")
print(f"  Dogs - Predicted: {pred_dogs_2023:.2f}, Actual: {test_y_dogs}, Accuracy: {accuracy_dogs_2023:.2%}")

print("\nFuture Predictions for 2024-2026:")
print(f"  Cats: {', '.join(f'{pred:.2f}' for pred in future_cats)}")
print(f"  Dogs: {', '.join(f'{pred:.2f}' for pred in future_dogs)}")
