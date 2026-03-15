# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:27:52 2020

@author: dell
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
#防止出现乱码
plt.rcParams['font.sans-serif']=['SimHei']#黑体
plt.rcParams['axes.unicode_minus'] = False
#[任务一]
def dataprocessing():

        try:
            filename=input('请输入要打开的文件名19.tmdb_5000_movies.csv:') #指定路径
            df=pd.read_csv(filename)  #读取文件
            print(df.head(3))  #查看前三行
            print(df.tail(2))  #查看后两行
            print('任务1执行成功！')
        except:  #打开文件失败时候执行的代码
            print('任务1执行失败')
#[任务二]
def  dataselection():
        try:
            filename=input('请输入要打开的文件名19.tmdb_5000_movies.csv:') #指定路径
            df=pd.read_csv(filename)  #读取文件
            df=df.dropna()#去除缺失值
            df_new=df.loc[:,['budget','id','release_date','revenue','title','original_language']]
            df_new.to_csv('tmdb_5000_movies_budgt_revenue.csv',index=False)
            print('任务2执行成功！')
        except:
            print('任务2执行失败')
#[任务三]
def readnew():
        try:
            filename=input('请输入要打开的文件名tmdb_5000_movies_budgt_revenue.csv:') #指定路径
            df_new=pd.read_csv(filename)  #读取文件
            df_newgood=df_new[df_new['original_language']=='en']
            df_newgood.to_csv('tmdb_5000_movies_budgt_revenue_en.txt',index=False)
            print('任务3执行成功!')
        except:
            print('任务3执行失败')
#[任务四]
def adddata():
        try:
            filename=input('请输入要打开的文件名tmdb_5000_movies_budgt_revenue_en.txt:') #指定路径
            df_newgood=pd.read_csv(filename,encoding='cp936') 
            df_newgood['Profit']=(df_newgood['revenue']-df_newgood['budget'])
            df_newgood.to_csv('tmdb_5000_movies_budgt_revenue_en_profit.csv',index=False,encoding='cp936')
            print('任务4执行成功！')
        except:
            print('任务4执行失败')
#[任务五]
def dataVisual():
        fileName = input('请输入要打开的文件名tmdb_5000_movies_budgt_revenue_en_profit.csv:')
        try:
            df_mean = pd.read_csv(fileName,encoding='cp936')
            df_mean = df_mean.loc[:,['title','budget']]
            df_mean=df_mean.sort_values(by='title',ascending=False)
            plt.figure(figsize=(50,5))
            plt.plot(range(len(list(df_mean['title']))),df_mean['budget'],color='red')               
            plt.xlabel('title',fontsize=12)
            xlength = len(df_mean)
            print('xlengtn=',xlength)
            xticksloc = [i for i in range(xlength)if i%200==0]
            print('xticksloc=',xticksloc)
            xtickslabels = df_mean['title'].values[::200]
            print('xtickslabels=',xtickslabels)
            plt.xticks(xticksloc,xtickslabels,rotation=90)
            plt.ylabel('budget',fontsize=16)
            plt.title('budget-title')
            plt.savefig('movies_en_budget_1990_2018.png',dpi=400)
            plt.show()
            
            df_mean = pd.read_csv(fileName,encoding='cp936')
            df_mean=df_mean.sort_values(by='title',ascending=False)
            df_mean = df_mean.loc[:,['title','revenue']]
            plt.figure(figsize=(50,5))
            plt.plot(range(len(list(df_mean['title']))),df_mean['revenue'],color='green')                  
            plt.xlabel('title',fontsize=12)
            xlength = len(df_mean)
            print('xlengtn=',xlength)
            xticksloc = [i for i in range(xlength)if i%200==0]
            print('xticksloc=',xticksloc)
            xtickslabels = df_mean['title'].values[::200]
            print('xtickslabels=',xtickslabels)
            plt.xticks(xticksloc,xtickslabels,rotation=90)
            plt.ylabel('revenue',fontsize=16)
            plt.title('revenue-title')
            plt.savefig('movies_en_revenue_1990_2018.png',dpi=400)
            plt.show()
            
            df_mean = pd.read_csv(fileName,encoding='cp936')
            df_mean=df_mean.sort_values(by='title',ascending=False)
            df_mean = df_mean.loc[:,['title','Profit']]
            plt.figure(figsize=(50,5))
            plt.plot(range(len(list(df_mean['title']))),df_mean['Profit'],color='blue')             
            plt.xlabel('title',fontsize=12)
            xlength = len(df_mean)
            print('xlengtn=',xlength)
            xticksloc = [i for i in range(xlength)if i%200==0]
            print('xticksloc=',xticksloc)
            xtickslabels = df_mean['title'].values[::200]
            print('xtickslabels=',xtickslabels)
            plt.xticks(xticksloc,xtickslabels,rotation=90)
            plt.ylabel('Profit',fontsize=16)
            plt.title('Profit-title')
            plt.savefig('movies_en_Profit_1990_2018.png',dpi=400)
            plt.show()
            print('任务5执行成功')
        except:
            print('任务5执行失败')
def menu():
    print('[任务选择]\n'
          '+--------1990-2018 年华语电影预算与收入数据分析 -------------+\n'
          '|0、退出。                                                   |\n'
          '|1、数据读取与预处理。                                        |\n'
          '|2、数据选择及导出。                                          |\n'
          '|3、数据定值选择。                                          |\n'
          '|4、添加数据。                                                |\n'
          '|5、数据可视化选择。                                          |\n'
          '+------------------------------------------------------------+')
#功能选择模块
def task():
    while True:
        menu()
        num=input('请输入任务选项：')
        if num=='1':
            dataprocessing()
        elif num=='2':
            if os.path.exists('19.tmdb_5000_movies.csv'):
                dataselection()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num=='3':
            if os.path.exists('tmdb_5000_movies_budgt_revenue.csv'):
                readnew()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num=='4':
            if os.path.exists('tmdb_5000_movies_budgt_revenue_en.txt'):
                adddata()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num=='5':
            if os.path.exists('tmdb_5000_movies_budgt_revenue_en_profit.csv'):
                dataVisual()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num=='0':
            print('程序结束！')
            break
        else:
            print('输入选项有误')
        input("回车显示菜单")
if __name__ == "__main__":  #主函数入口
    task()#调用功能选择函数    
            
            
            
 