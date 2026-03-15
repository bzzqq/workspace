import scipy.stats as stats
import math
# 定义参数
p_nominal = 0.1  # 标称次品率
alpha_1 = 0.05   # 95% 置信水平对应的 α 值
alpha_2 = 0.1    # 90% 置信水平对应的 α 值
delta_1 = 0.05   # 情形1的误差限
delta_2 = 0.05   # 情形2的误差限


# 计算样本量的函数
def calculate_sample_size(p, alpha, delta):
    z_alpha = stats.norm.ppf(1 - alpha/2)
    n = (z_alpha ** 2) * p * (1 - p) / (delta ** 2)
    return math.ceil(n)


# 计算样本量
sample_size_95 = calculate_sample_size(p_nominal, alpha_1, delta_1)
sample_size_90 = calculate_sample_size(p_nominal, alpha_2, delta_2)

print(f"95% 置信水平下需要的样本量: {sample_size_95}")
print(f"90% 置信水平下需要的样本量: {sample_size_90}")
