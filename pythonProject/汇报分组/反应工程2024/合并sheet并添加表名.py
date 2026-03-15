import pandas as pd
import random

# 读取 Excel 文件
xls = pd.ExcelFile('/home/bz/workspace/pythonProject/汇报分组/反应工程2024/分组名单.xlsx')

# 获取工作表名称列表
with pd.ExcelFile('/home/bz/workspace/pythonProject/汇报分组/反应工程2024/分组名单.xlsx') as xls:
    sheet_names = xls.sheet_names
    # sheet_names.sort()
    random.shuffle(sheet_names)
    print(sheet_names)

# 创建一个空的 DataFrame 列表，用于存储每个工作表的数据
worksheets = []

# 遍历工作表并添加一列工作表名称
for sheet_name in sheet_names:
    # 读取工作表数据
    df = pd.read_excel('/home/bz/workspace/pythonProject/汇报分组/反应工程2024/分组名单.xlsx', sheet_name=sheet_name)

    # 添加一列工作表名称
    df['Worksheet'] = sheet_name

    # 将数据添加到工作表列表中
    worksheets.append(df)

# 将所有工作表数据合并为一个 DataFrame
merged_df = pd.concat(worksheets, ignore_index=True)

# 输出合并后的 DataFrame
print(merged_df)

# 保存合并后的 DataFrame 到新的 Excel 文件
merged_df.to_excel('反应工程分组.xlsx', index=False)