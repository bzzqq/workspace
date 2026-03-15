# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# 防止出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False


# [任务一]
def dataprocessing():
        try:
            filename = input('请输入要打开的文件名10.world_pm25_pm10.csv:')  # 指定路径
            df = pd.read_csv(filename, encoding='cp936')  # 读取文件
            print(df.head(3))  # 查看前三行
            print(df.tail(2))  # 查看后两行
            print('任务1执行成功！')
        except:  # 打开文件失败时候执行的代码
            print('任务1执行失败')


# [任务二]
def dataselection():
        try:
            filename = input('请输入要打开的文件名10.world_pm25_pm10.csv:')  # 指定路径
            df = pd.read_csv(filename, encoding='cp936')  # 读取文件
            df_new = df.loc[:, ['Region', 'Country', 'City/station', 'PM10', 'PM10 Year']]
            df_new = df_new.dropna()
            df_new.to_csv('world_pm10.txt',sep=' ',index = False)
            print('任务2执行成功！')
        except:
            print('任务2执行失败')


# [任务三]
def readnew():
        try:
            filename = input('请输入要打开的文件名world_pm10.txt:')  # 指定路径
            df_new = pd.read_csv(filename, encoding='cp936',sep=' ')  # 读取文件
            df3 = df_new[(df_new['Region']== 'Wpr') & (df_new['PM10 Year'] == '2012')]
            X = [i[1] for i in list(df3['City/station'].items())]
            Y = [i[1] for i in list(df3['PM10'].items())]
            plt.figure()
            for x,y,label in zip(range(len(X)),Y,X):                    #分别读取x轴、y轴、颜色、标签
                plt.bar(x,y,color='r',label=label)
            #添加刻度标签
            plt.xticks(range(len(X)),X,rotation=45)
            #添加标题
            plt.title('PM10-City/station')
            #添加轴标签
            plt.ylabel('PM10')
            plt.legend()
            plt.show()
            print('任务3执行成功!')
        except:
            print('任务3执行失败')


# [任务四]
def adddata():
        try:
            filename = input('请输入要打开的文件名world_pm10.txt:')  # 指定路径
            df2 = pd.read_csv(filename, encoding='cp936',sep=' ')
            df4 = df2.loc[:, ['City/station', 'PM10', 'PM10 Year']]
            df4 = df4.sort_values(by='PM10',ascending=False)
            df4.to_csv('world_pm10_city.csv',sep=' ', index = False)
            print('任务4执行成功！')
        except:
            print('任务4执行失败')


# [任务五]
def dataVisual():
        fileName = input('请输入要打开的文件名world_pm10_city.csv:')
        try:
            df5 = pd.read_csv(fileName,sep=' ')
            category = [0, 50, 100,150,200]
            labels = ['One', 'Two', 'Three', 'Four']
            df6 = pd.cut(df5['PM10'], category, right=False, labels=labels)
            #df7 = pd.concat([df5,df6],axis=1)
            plt.figure()
            plt.pie([i[1] for i in list(df6.value_counts().items())],
                    labels=labels)
            plt.savefig('world_pm10_city _pie.png',dpi=300)
            plt.show()
            print('任务5执行成功')
        except:
            print('任务5执行失败')


def menu():
    print('[任务选择]\n'
          '+--------1990-2018 -------------+\n'
          '|0、退出。                                                   |\n'
          '|1、数据读取。                                        |\n'
          '|2、数据预处理并选择及导出。                                          |\n'
          '|3、数据计算与添加。                                          |\n'
          '|4、文件转换。                                                |\n'
          '|5、数据可视化选择。                                          |\n'
          '+------------------------------------------------------------+')


# 功能选择模块
def task():
    while True:
        menu()
        num = input('请输入任务选项：')
        if num == '1':
            dataprocessing()
        elif num == '2':
            if os.path.exists('10.world_pm25_pm10.csv'):
                dataselection()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '3':
            if os.path.exists('world_pm10.txt'):
                readnew()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '4':
            if os.path.exists('world_pm10.txt'):
                adddata()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '5':
            if os.path.exists('world_pm10_city.csv'):
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
