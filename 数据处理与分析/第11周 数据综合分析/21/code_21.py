# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import os

# 防止出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False


# 任务一
def dataReading():

    fileName = input('请输入要打开的文件名21.movies.csv:')  # 读取数据
    try:
        df = pd.read_csv(fileName, encoding='cp936')
        print(df.head(3))  # 查看前三行
        print(df.tail(2))  # 查看后三行
        print("任务一执行成功!")
    except:
        print('任务一执行不成功')  # 打开文件失败时执行的代码


# 任务二
def dataPreprocessing():
    fileName = input('请输入要打开的文件名21.movies.csv:')  # 读取数据
    try:
        df = pd.read_csv(fileName, encoding='cp936')
        df = df.dropna()  # 丢弃缺失值
        df_new = df.loc[:, ['Budget', 'Release Year', 'Revenue', 'Title', 'Starring Actors Popularity']]
        df_new.to_csv('movies_revenue_starring.csv', encoding='cp936', index=False, sep=' ')
        print("任务二执行成功")
    except:
        print('任务二执行不成功')  # 打开文件失败时执行的代码


# 任务三
def dataSelection():
    fileName = input('请输入要打开的文件名movies_revenue_starring.csv:')
    # 读取数据
    try:
        df_new = pd.read_csv(fileName, encoding='cp936', sep=' ')
        df_newGood = df_new[(df_new['Release Year'] > 1950) & (df_new['Release Year'] < 2020)]
        df_newGood.to_csv('movies_revenue_starring_1950_2010.txt', encoding='cp936', index=False)
        print("任务三执行成功!")
    except:
        print('任务三执行不成功')  # 打开文件失败时执行的代码


# 任务四
def dataCalculate():
    fileName = input('请输入要打开的文件名movies_revenue_starring_1950_2010.txt:')
    # 读取数据
    try:
        df_newGood = pd.read_csv(fileName, encoding='cp936')
        df_newGood.to_excel('movies_revenue_starring_1950_2010.xlsx', encoding='cp936', index=False)
        print("任务四执行成功!")
    except:
        print('任务四执行不成功')  # 打开文件失败时执行的代码


# 任务五
def dataVisual():
    fileName = input('请输入要打开的文件名movies_revenue_starring_1950_2010.txt:')
    try:
        df_mean = pd.read_csv(fileName, encoding='cp936')
        df_mean = df_mean.loc[:, ['Title', 'Revenue']]
        df_mean = df_mean.sort_values(by='Title', ascending=False)
        plt.figure(figsize=(50, 5))
        plt.plot(range(len(list(df_mean['Title']))), df_mean['Revenue'], color='red')
        plt.xlabel('Title', fontsize=12)
        xlength = len(df_mean)
        print('xlengtn=', xlength)
        xticksloc = [i for i in range(xlength) if i % 300 == 0]
        print('xticksloc=', xticksloc)
        xtickslabels = df_mean['Title'].values[::300]
        print('xtickslabels=', xtickslabels)
        plt.xticks(xticksloc, xtickslabels, rotation=45)  # 刻标，标签，角度
        plt.ylabel('Revenue', fontsize=16)
        plt.savefig('movies_revenue_1950_2010.png', dpi=400)
        plt.show()

        df_mean = pd.read_csv(fileName, encoding='cp936')
        df_mean = df_mean.sort_values(by='Title', ascending=False)
        df_mean = df_mean.loc[:, ['Title', 'Starring Actors Popularity']]
        plt.figure(figsize=(50, 5))
        plt.plot(range(len(list(df_mean['Title']))), df_mean['Starring Actors Popularity'], color='green')
        plt.xlabel('Title', fontsize=12)
        xlength = len(df_mean)
        print('xlengtn=', xlength)
        xticksloc = [i for i in range(xlength) if i % 300 == 0]
        print('xticksloc=', xticksloc)
        xtickslabels = df_mean['Title'].values[::300]
        print('xtickslabels=', xtickslabels)
        plt.xticks(xticksloc, xtickslabels, rotation=45)
        plt.ylabel('Starring Actors Popularity', fontsize=16)
        plt.savefig('movies_starpopularity_1950_2010.png', dpi=400)
        plt.show()
        print('任务五执行成功')
    except:
        print('任务五执行失败')


def menu():
    print('[任务选择]\n'
          '+--------1916-2016年电影票房与主演演员人气数据分析-------------+\n'
          '|0、退出。                                                   |\n'
          '|1、数据读取。                                        |\n'
          '|2、数据预处理并选择及导出。                                           |\n'
          '|3、数据计算与添加。                                          |\n'
          '|4、数据可视化选择1。                                             |\n'
          '|5、数据可视化选择2。                                             |\n'
          '+------------------------------------------------------------+')


# 功能选择模块
def task():
    while True:
        menu()
        num = input('请输入任务选项：')
        if num == '1':
            dataReading()
        elif num == '2':
            if os.path.exists('21.movies.csv'):
                dataPreprocessing()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '3':
            if os.path.exists('movies_revenue_starring.csv'):
                dataSelection()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '4':
            if os.path.exists('movies_revenue_starring_1950_2010.txt'):
                dataCalculate()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '5':
            if os.path.exists('movies_revenue_starring_1950_2010.txt'):
                dataVisual()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '0':
            print('程序结束！')
            break
        else:
            print('输入选项有误')
        input("回车显示菜单")


if __name__ == "__main__":  # 主函数入口
    task()  # 调用功能选择函数
