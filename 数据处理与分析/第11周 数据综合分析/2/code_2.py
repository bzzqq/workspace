# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import os

# 防止中文出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False


# 任务【1】
def datapreprocessing():
    filename = input('请输入要打开的文件名2.pollution_us_5city_2006_2010_SO2.csv:')  # 打开文件
    try:
        df = pd.read_csv(filename, encoding='cp936')  # 读取数据
        print(df.head(5))  # 查看前五行内容
        print(df.tail(2))  # 查看后两行内容
        print('任务1执行成功！')
    except:  # 任务执行不成功时输出的代码
        print('任务1执行不成功！')


# 任务【2】
def dataconduction():
    filename = input('请输入要打开的文件名2.pollution_us_5city_2006_2010_SO2.csv：')  # 打开文件
    try:
        df = pd.read_csv(filename, encoding='cp936')  # 读取数据
        print(df.columns[df.isnull().sum() > 0])
        for column in list(df.columns[df.isnull().sum() > 0]):  # 筛选需要填充的列
            mean_val = df[column].mean()
            df[column].fillna(mean_val, inplace=True)
        df_new = df.drop(columns=['State Code', 'County Code', 'Site Num', 'Address'])
        df_new.to_csv('pollution_us_5city_2006_2010_SO2.xlsx', index=False)
        print("任务2执行成功！")
    except:
        print("任务2执行不成功")


# 任务【3】
def dataselection():
    filename = input('请输入要打开的文件名pollution_us_5city_2006_2010_SO2.xlsx：')
    try:
        df = pd.read_csv(filename, encoding='cp936')
        df_new = df[df['City'] == 'New York']
        df_new.to_csv('pollution_us_NewYork_2006_2010_SO2.txt', encoding='cp936', index=False, sep=' ')  #错误：未使用空格间隔
        print("任务3执行成功！")
        #break
    except:
        print("任务3执行失败！")


# 任务【4】
def datainventory():
    filename = input('请输入要打开的文件名pollution_us_NewYork_2006_2010_SO2.txt：')
    try:
        df = pd.read_csv(filename, encoding='cp936', sep=' ')
        df['year'] = df['Date Local'].map(lambda x: int(x[0:x.index('/')]))
        df_new1 = df[df.year > 2006]
        df_new2 = df_new1[df_new1.year < 2010]
        df_new2.to_csv('pollution_us_NewYork_2007_2009_SO2.csv', encoding='cp936', index=False)
        print("任务4执行成功！")
    except:
        print("任务4执行失败！")


# 任务【5】
def datavisualization():
    filename = input('请输入要打开的文件名pollution_us_NewYork_2007_2009_SO2.csv：')
    try:
        df = pd.read_csv(filename, encoding='cp936')
        df['year'] = df['Date Local'].map(lambda x: int(x[0:x.index('/')]))
        df['month'] = df['Date Local'].map(lambda x: int(x[5:x.rindex('/')]))
        df_mean1 = df.loc[:, ['SO2 Mean', 'year', 'month']]
        df_mean2 = df.loc[:, ['SO2 1st Max Hour', 'year', 'month']]
        df_mean3 = df.loc[:, ['SO2 AQI', 'year', 'month']]
        df_mean1_groupby = df_mean1.groupby(['year', 'month'], as_index=False).mean()
        df_mean2_groupby = df_mean2.groupby(['year', 'month'], as_index=False).mean()
        df_mean3_groupby = df_mean3.groupby(['year', 'month'], as_index=False).mean()
        df1 = df_mean1_groupby.sort_values(['year', 'month'])  # 按照月份从小到大排序
        df2 = df_mean2_groupby.sort_values(['year', 'month'])  # 按照月份从小到大排序
        df3 = df_mean3_groupby.sort_values(['year', 'month'])  # 按照月份从小到大排序
        df1.to_csv('SO2_Mean.csv', encoding='cp936', index=False)  # 将月平均放到一个新的csv文件中方便作图
        df2.to_csv('SO2_1st_Max_Hour.csv', encoding='cp936', index=False)  # 将月平均放到一个新的csv文件中方便作图
        df3.to_csv('SO2_AQI.csv', encoding='cp936', index=False)  # 将月平均放到一个新的csv文件中方便作图
        try:
            df_new1 = pd.read_csv('SO2_Mean.csv', encoding='cp936')  # 读文件
            print(df_new1)
            df_new1['SO2 Mean1'] = df_new1['SO2 Mean'].map(lambda x: float(x))
            df_new1['year-month'] = df_new1['year'].map(lambda x: str(x)) + '-' + df_new1['month'].map(lambda x: str(x))
            print(df_new1['year-month'])
            plt.figure(figsize=(12, 8))  # 作图的大小
            plt.plot(range(len(list(df_new1['year-month']))), df_new1['SO2 Mean1'], color='red', marker='o', label='SO2 Mean')
            plt.xticks(range(len(list(df_new1['year-month']))), list(df_new1['year-month']), rotation=90)
            plt.title('2007--2009年的SO2月均值', fontproperties='SimHei', fontsize=14)
            plt.xlabel('X-每年的月份', fontproperties='SimHei', fontsize=14)
            plt.ylabel('Y-月平均值', fontproperties='SimHei', fontsize=14)
            plt.legend()
            plt.savefig('SO2_Mean.png', dpi=300)
            plt.show()

            df_new2 = pd.read_csv('SO2_1st_Max_Hour.csv', encoding='cp936')  # 读文件

            df_new2['SO2 1st Max Hour2'] = df_new2['SO2 1st Max Hour'].map(lambda x: float(x))
            df_new2['year-month'] = df_new2['year'].map(lambda x: str(x)) + '-' + df_new2['month'].map(lambda x: str(x))
            plt.figure(figsize=(12, 8))  # 作图的大小
            plt.plot(range(len(list(df_new2['year-month']))), df_new2['SO2 1st Max Hour2'], color='green', marker='o', label='SO2 1st Max Hour')
            plt.xticks(range(len(list(df_new2['year-month']))), list(df_new2['year-month']), rotation=90)
            plt.title('2007--2009年的SO2 1st Max Hour的月均值', fontproperties='SimHei', fontsize=14)
            plt.xlabel('X-每年的月份', fontproperties='SimHei', fontsize=14)
            plt.ylabel('Y-月平均值', fontproperties='SimHei', fontsize=14)
            plt.legend()
            plt.savefig('SO2_1st_Max_Hour.png', dpi=300)
            plt.show()

            df_new3 = pd.read_csv('SO2_AQI.csv', encoding='cp936')  # 读文件
            df_new3['SO2 AQI3'] = df_new3['SO2 AQI'].map(lambda x: float(x))
            df_new3['year-month'] = df_new3['year'].map(lambda x: str(x)) + '-' + df_new3['month'].map(lambda x: str(x))
            plt.figure(figsize=(12, 8))  # 作图的大小
            plt.plot(range(len(list(df_new3['year-month']))), df_new3['SO2 AQI3'], color='blue', marker='o', label='SO2 AQI')
            plt.xticks(range(len(list(df_new3['year-month']))), list(df_new3['year-month']), rotation=90)
            plt.title('2007--2009年的SO2 AQI月均值', fontproperties='SimHei', fontsize=14)
            plt.xlabel('X-每年的月份', fontproperties='SimHei', fontsize=14)
            plt.ylabel('Y-月平均值', fontproperties='SimHei', fontsize=14)
            plt.legend()
            plt.savefig('SO2 AQI.png', dpi=300)
            plt.show()
            print('任务5执行成功！')
        except:
            print("任务5执行失败！")
    except:
        print('任务5执行失败！')


# 系统主界面
def menu():
    print('[任务选择]\n'
          '+-----美国五个著名城市空气质量分析及可视化系统----+\n'
          '|0、退出。                                    |\n'
          '|1、数据读取。                          |\n'
          '|2、数据预处理及导出。                            |\n'
          '|3、数据选择及导出。                            |\n'
          '|4、数据选择及转存。                             |\n'
          '|5、数据可视化。                                |\n'
          '+---------------------------------------------+')


# 功能选择模块
def task():
    while True:
        menu()  # 打印系统主界面
        num = input("请输入任务选项：")
        if num == '1':
            datapreprocessing()
        elif num == '2':
            if os.path.exists('2.pollution_us_5city_2006_2010_SO2.csv'):
                dataconduction()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '3':
            if os.path.exists('pollution_us_5city_2006_2010_SO2.xlsx'):
                dataselection()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '4':
            if os.path.exists('pollution_us_NewYork_2006_2010_SO2.txt'):
                datainventory()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '5':
            if os.path.exists('pollution_us_NewYork_2007_2009_SO2.csv'):
                datavisualization()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '0':
            print('整个程序执行结束！')
            break
        else:
            print("输入的选项有误，请重新输入！")
        input("请回车以显示菜单")


# 主函数
if __name__ == '__main__':
    task()  # 调用功能选择函数
