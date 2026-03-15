# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 13:11:30 2020

@author: 阿七
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

#防止中文乱码
plt.rcParams['font.sans-serif']=['SimHei'] #黑体
plt.rcParams['axes.unicode_minus']=False

#【任务一】
def dataPreprocessing():
        #读取数据
        fn = input('请输入所要打开的文件名称30.bike_day.csv：')
        try:
            df = pd.read_csv(fn)
            #查看前五行
            print(df.head(5))
            #查看后两行
            print(df.tail(2))           
            print('任务一执行完成！')
        except:              #若文件打开失败使执行的代码
            print('任务一执行失败！')

#【任务二】
def dataSelection():
        #读取数据
        fn = input('请输入所要打开的文件名称30.bike_day.csv:')
        try:
            df = pd.read_csv(fn)
            df = df.dropna()#丢弃缺失值
            df_Selection = df.loc[:,['instant','dteday','windspeed','casual','registered']]
            try:
                df_Selection.to_csv('bike_windspeed_user.txt',index=False,sep=' ') #以空格为数据间的分隔符
                print('任务二执行完成！')
            except:         #若新文件导出失败时执行的代码
                print('文件导出失败！')
        except:             #若文件打开失败时执行的代码
            print('任务二执行失败！')

#【任务三】
def dataExtraction():
        #读取数据
        fn = input('请输入所要打开的文件名称bike_windspeed_user.txt:')
        try:
            df = pd.read_csv(fn,sep=' ') #读取时以空格为分隔符
            df['cnt'] = (df['casual'] + df['registered']) #直接生成新列‘cnt’，其值为该两列数据之和
            df.to_excel('bike_windspeed_user_cnt.xlsx',index=False)
            print('任务三执行完成！')
        except:             #若文件打开失败时执行的代码        
            print('任务三执行失败！')
            
#【任务四】
def dataConsolidation():
        #读取数据
        fn = input('请输入所要打开的文件名称bike_windspeed_user_cnt.xlsx:')
        try:
            df = pd.read_excel(fn)
            df_describe = df.describe() #利用describe的返回值获取‘cnt’列的最大值和最小值和均值
            maxValue = df_describe.at['max','windspeed']
            minValue = df_describe.at['min','windspeed']
            meanValue = df_describe.at['mean','windspeed']
            print('maxValue = ',maxValue)
            print('minValue = ',minValue)
            print('meanValue = ',meanValue)
            category = [minValue,0.3,0.35,0.4,maxValue]
            labels = ['Normal','Little','Big','Strong'] 
            df['Label'] = pd.cut(df['windspeed'], category, right=False, labels=labels) 
            df.to_csv('bike_windspeed_user_cnt_result.csv',index=False)
            print('任务四执行完成！')
        except:             #若文件打开失败时执行的代码
            print('任务四执行失败！')

#【任务五】
def dataVisualization():
        #读取数据
        fn = input('请输入所要打开的文件名称bike_windspeed_user_cnt_result.csv:')
        try:
            df = pd.read_csv(fn)
            df_windspeed = df.loc[:,['cnt','Label']]
            df_windspeed = df_windspeed.groupby(by='Label',as_index=False).mean()            
            df_windspeed.plot(x='Label',kind='bar',figsize=(12,8),grid=0.1) #作柱状图
            plt.title('2011-2012 年不同风速下的共享单车租赁用户日均数量统计图') #命名标题
            plt.xlabel('风速') #设置横轴标签为风速
            plt.ylabel('租赁用户数量') #设置纵轴标签为租赁用户数量
            plt.savefig('bike_windspeed_user_cnt.png',dpi=400) #保存图片
            plt.show()
            print('任务五执行完成！')
        except:             #若文件打开失败时执行的代码
            print('任务五执行失败！')

#系统主界面
def menu():
    print('                             【任务选择】\n'
          '—————————————2011-2012年共享单车租赁用户数据分析及可视化系统————————————\n'
          '|0.退出数据处理系统                                                   |\n'
          '|1.数据读取                                                   |\n'
          '|2.数据的预处理并挑取及导出                                                   |\n'
          '|3.每日租赁用户汇总                                                   |\n'
          '|4.数据计算及其统计                                                   |\n' 
          '|5.数据日均值可视化                                                   |\n'
          '—————————————————————————————————————————————————————————————————————')
    
#功能选择模块
def task():
    while True:
        menu() #打印出操作菜单
        num = input('请输入所要执行的任务编号:')
        if num == '1':
            dataPreprocessing()
        elif num == '2':
            dataSelection()
        elif num == '3':
            if os.path.exists('bike_windspeed_user.txt'):
                dataExtraction()
            else:
                print('当前不能执行该任务，请先确定是否已执行前面的任务！')
        elif num == '4':
            if os.path.exists('bike_windspeed_user_cnt.xlsx'):
                dataConsolidation()
            else:
                print('当前不能执行该任务，请先确定是否已执行前面的任务！')
        elif num == '5':
            if os.path.exists('bike_windspeed_user_cnt_result.csv'):
                dataVisualization()
            else:
                print('当前不能执行该任务，请先确定是否已执行前面的任务！')
        elif num == '0':
            print('已退出数据处理系统')
            break
        else:
            print('输入编号有误！')
        input('按回车显示操作菜单')
        
#主函数
if __name__ =='__main__':
    task() #调用任务选择函数
    
