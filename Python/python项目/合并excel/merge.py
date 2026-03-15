import os
import pandas as pd

excels = [
    pd.read_excel(fname) for fname in os.listdir("./") if ".xlsx" in fname
]  # os.listdir可以列出目录下的所有文件
df = pd.concat(excels)  # pd.concat方法可以批量合并excel对象
df.to_excel("结果文件.xlsx", index=False)
