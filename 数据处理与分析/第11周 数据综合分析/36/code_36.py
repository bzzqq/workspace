# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:31:12 2020

@author: 阿七
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

# 防止中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False


# 【任务一】
def dataPreprocessing():
        # 读取数据
        fn = input('请输入所要打开的文件名称36.2007_household_power_consumption.csv:')        
        try:
            df = pd.read_csv(fn)
            # 查看前五行
            print(df.head(5))
            # 查看后两行
            print(df.tail(2))
            print('任务一执行完成！')
        except :  # 若文件打开失败使执行的代码
            print('任务一执行失败！')


# 【任务二】
def dataSelection():
        # 读取数据
        fn = input('请输入所要打开的文件名称36.2007_household_power_consumption.csv:')      
        try:
            df = pd.read_csv(fn)
            df = df.dropna()
            df_Selection = df.loc[:, ['Date', 'Time', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']]
            try:
                #df_Selection.to_csv('2007_household_power_consumption_sub.txt', index=False, sep=' ')  # 以空格为数据间的分隔符
                df_Selection.to_csv('2007_household_power_consumption_sub_test_01.txt', index=False, sep=' ')  # 以空格为数据间的分隔符
                print('任务二执行完成！')
            except:  # 若新文件导出失败时执行的代码
                print('文件导出失败！')
        except:  # 若文件打开失败时执行的代码
            print('任务二执行失败！')


# 【任务三】
def dataExtraction_1():
        # 读取数据
        fn = input('请输入所要打开的文件名称2007_household_power_consumption_sub.txt:')        
        try:
            df = pd.read_csv(fn, sep=' ')  # 读取时以空格为分隔符                   
            df_date = df.groupby(by='Date', as_index=False).sum()  # 对三列数据求和                     
            df_date.to_excel('2007_household_power_consumption_day.xlsx', index=False)            
            print('任务三执行完成！')
        except:  # 若文件打开失败时执行的代码
            print('任务三执行失败！')


# 【任务四】
def dataVisualization_1():
        # 读取数据
        fn = input('请输入所要打开的文件名称2007_household_power_consumption_day.xlsx:')
        try:
            df = pd.read_excel(fn)
            df.plot(x='Date', kind='bar', figsize=(24, 10), grid=0.1)  # 作柱状图
            plt.title('2007年7月各机器用电功率统计图')  # 命名标题
            plt.xlabel('日期')  # 设置横轴标签
            plt.ylabel('用电功率（瓦特每小时）')  # 设置纵轴标签
            plt.savefig('2007_household_power_consumption_day.jpg', dpi=400)  # 保存图片
            plt.show()
            print('任务四执行完成！')
        except:  # 若文件打开失败时执行的代码
            print('任务四执行失败！')


# 【任务五】
def dataExtraction_2():
        # 读取数据
        fn = input('请输入所要打开的文件名称2007_household_power_consumption_day.xlsx:')        
        try:
            df = pd.read_excel(fn)
            df['总耗电量'] = df['Sub_metering_1'] + df['Sub_metering_2'] + df['Sub_metering_3']  # 添加新列
            df['平均耗电量'] = df['总耗电量'] / 3.0  # 添加新列
            df.to_excel('2007_household_power_consumption_day2.xlsx', index=False)
            print('任务五执行成功！')
        except:  # 若文件打开失败时执行的代码
            print('任务五执行失败！')


# 【任务六】
def dataVisualization_2():
        # 读取数据
        fn = input('请输入所要打开的文件名称2007_household_power_consumption_day2.xlsx:')       
        try:

            df = pd.read_excel(fn)
            df_sum = df.loc[:, ['Date', '总耗电量']]
            df_sum.plot(x='Date', kind='line', figsize=(12, 8), color='Red', grid=0.1)  # 作折线图
            plt.title("2007年7月每日总耗电量")
            plt.xlabel('日期')
            plt.ylabel('总耗电量')
            plt.savefig("2007_household_power_consumption_daysum.jpg", dpi=400)  # 保存图片
            plt.show()

            df_mean = df.loc[:, ['Date', '平均耗电量']]
            df_mean.plot(x='Date', kind='line', figsize=(12, 8), color='Blue', grid=0.1)  # 作折线图
            plt.title("2007年7月每日平均耗电量")
            plt.xlabel('日期')
            plt.ylabel('平均耗电量')
            plt.savefig("2007_household_power_consumption_daymean.jpg", dpi=400)  # 保存图片
            plt.show()
            print('任务六执行成功！')
        except:  # 打开文件失败时执行的代码
            print('任务六执行失败！')

# 系统主界面
def menu():
    print('                             【任务选择】\n'
          '————————————————2007年7月居民家庭用电数据分析及可视化系统———————————————\n'
          '|0.退出数据处理系统                                                   |\n'
          '|1.数据读取                                                   |\n'
          '|2.数据的预处理并挑取及导出                                                   |\n'
          '|3.对数据分类及汇总                                                   |\n'
          '|4.不同电器通电功率的数据可视化                                        |\n'
          '|5.对每日耗电量整理                                                   |\n'
          '|6.每日耗电量数据的可视化                                             |\n'
          '—————————————————————————————————————————————————————————————————————')


# 功能选择模块
def task():
    while True:
        menu()  # 打印出操作菜单
        num = input('请输入所要执行的任务编号:')
        if num == '1':
            dataPreprocessing()
        elif num == '2':
            dataSelection()
        elif num == '3':
            if os.path.exists('2007_household_power_consumption_sub.txt'):
                dataExtraction_1()
            else:
                print('当前不能执行该任务，请先确定是否已执行前面的任务！')
        elif num == '4':
            if os.path.exists('2007_household_power_consumption_day.xlsx'):
                dataVisualization_1()
            else:
                print('当前不能执行该任务，请先确定是否已执行前面的任务！')
        elif num == '5':
            if os.path.exists('2007_household_power_consumption_day.xlsx'):
                dataExtraction_2()
            else:
                print('当前不能执行该任务，请先确定是否已执行前面的任务！')
        elif num == '6':
            if os.path.exists('2007_household_power_consumption_day2.xlsx'):
                dataVisualization_2()
            else:
                print('当前不能执行该任务，请先确定是否已执行前面的任务！')
        elif num == '0':
            print('已退出数据处理系统')
            break
        else:
            print('输入编号有误！')
        input('按回车显示操作菜单')


# 主函数
if __name__ == '__main__':
    task()  # 调用任务选择函数
