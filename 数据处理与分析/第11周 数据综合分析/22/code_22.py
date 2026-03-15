# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# 防止中文出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False


# 任务一
def dataPreprocessing():
        # 读取数据
        fileName = input('请输入要打开的文件名22.movies.csv：')
        try:
            df = pd.read_csv(fileName, encoding='cp936')
            # 查看前三行
            print(df.head(3))
            # 查看后两行
            print(df.tail(2))
            print("任务1执行成功!")
        except:  # 打开文件失败时执行的代码
            print('任务一执行不成功')


# 任务二
def dataSelection():
        # 读取数据
        fileName = input('请输入要打开的文件名22.movies.csv：')
        try:
            df = pd.read_csv(fileName, encoding='cp936')
            # 丢失缺失值
            df = df.dropna()
            df.to_csv('movies.csv', encoding='cp936', index=False,sep=' ')
            df_1 = df.loc[:, ['Budget', 'Release Year', 'Revenue', 'Title', 'Starring Actors Popularity']]
            df_1.to_csv('movies_revenue_starring.csv', encoding='cp936', index=False,sep=' ')
            print("任务二执行成功！")
        except:  # 打开文件失败时执行的代码
            print('任务二执行不成功')


# 任务三
def dataGroup():
        # 读取数据
        fileName = input('请输入要打开的文件名movies_revenue_starring.csv:')
        try:
            df_new = pd.read_csv(fileName, encoding='cp936',sep=' ')
            df_new2 = df_new[(df_new['Release Year'] > 1950) & (df_new['Release Year'] < 2010)]
            df_new2.to_csv('movies_revenue_starring_1950_2010.txt',sep=',',index=False,encoding='cp936')
            print('任务3执行成功!')
        except:  # 打开文件失败时执行的代码
            print('任务三执行不成功')


# 任务四
def dataCalculate():
        # 读取数据
        fileName = input('请输入要打开的文件名movies_revenue_starring_1950_2010.txt：')
        try:
            df_new = pd.read_csv(fileName, encoding='cp936')
            df_new['Profit'] = (df_new['Revenue'] - df_new['Budget'])
            df_new.to_csv('movies_revenue_starring_1950_2010_profit.csv', encoding='cp936',sep=' ',index=False)
            print('任务四执行成功!')
        except:  # 打开文件失败时执行的代码
            print('任务四执行不成功')


# 任务五
def dataDescribeVisualization():
        # 读取数据
        fileName = input('请输入要打开的文件名movies_revenue_starring_1950_2010_profit.csv:')
        try:
            df_new = pd.read_csv(fileName, encoding='cp936',sep=' ')
            df_new = df_new.loc[:, ['Title', 'Starring Actors Popularity']]
            df_new=df_new.sort_values(by='Title', ascending=True)
            plt.figure(figsize=(50,5))
            plt.plot(range(len(list(df_new['Title']))),df_new['Starring Actors Popularity'],color='red')
            plt.xlabel('Title', fontsize=12)  # 横坐标
            xlength = len(df_new)  # 数据长度
            print('xlength=', xlength)  # 抽样显示
            xticksloc = [i for i in range(xlength) if i % 350 == 0]
            print('xticksloc=', xticksloc)
            xtickslabels = df_new['Title'].values[::350]  # 显示标签
            print('xtickslabels=', xtickslabels)
            plt.xticks(xticksloc, xtickslabels, rotation=45)  # 45度倾斜显示
            plt.ylabel('Starring Actors Popularity', fontsize=16)
            plt.title('movies_starpopularity_1950_2010')
            plt.savefig('movies_starpopularity_1950_2010.png', dpi=400)
            plt.show()

            df_new = pd.read_csv(fileName, encoding='cp936',sep=' ')
            df_new=df_new.sort_values(by='Title', ascending=True)
            df_new = df_new.loc[:, ['Title', 'Profit']]
            plt.figure(figsize=(50,5))
            plt.plot(range(len(list(df_new['Title']))),df_new['Profit'],color='green')
            plt.xlabel('Title', fontsize=12)  # 横坐标
            xlength = len(df_new)  # 数据长度
            print('xlength=', xlength)  # 抽样显示
            xticksloc = [i for i in range(xlength) if i % 350 == 0]
            print('xticksloc=', xticksloc)
            xtickslabels = df_new['Title'].values[::350]  # 显示标签
            print('xtickslabels=', xtickslabels)
            plt.xticks(xticksloc, xtickslabels, rotation=45)  # 45度倾斜显示
            plt.ylabel('Profit', fontsize=16)
            plt.title('movies_profit_1950_2010')
            plt.savefig('movies_profit_1950_2010.png', dpi=400)
            plt.show()
            print('任务五执行成功!')
        except:  # 打开文件失败时执行的代码
            print('任务五执行不成功')


# 系统主界面
def menu():
    print('【任务选择】\n'
          '+----1916-2016 年电影盈利与主演演员人气数据分析---------+\n'
          '|0、退出程序                                     |\n'
          '|1、数据读取及查看                                |\n'
          '|2、数据处理及导出                                |\n'
          '|3、数据分类汇总                                  |\n'
          '|4、数据计算                                      |\n'
          '|5、数据排序及数据可视化                          |\n'
          '+-----------------------------------------------------+')


# 功能选择模块
def task():
    while True:
        menu()  # 打印系统主界面
        num = input("请输入任务选项：")
        if num == '1':
            dataPreprocessing()
        elif num == '2':
            if os.path.exists('22.movies.csv'):
                dataSelection()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '3':
            if os.path.exists('movies_revenue_starring.csv'):
                dataGroup()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '4':
            if os.path.exists('movies_revenue_starring_1950_2010.txt'):
                dataCalculate()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '5':
            if os.path.exists('movies_revenue_starring_1950_2010_profit.csv'):
                dataDescribeVisualization()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '0':
            print('程序结束！')
            break
        else:
            print('输入选项有误')
        input("回车显示菜单")


# 主函数
if __name__ == '__main__':
    task()  # 调用选择函数
