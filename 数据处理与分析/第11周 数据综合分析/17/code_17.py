# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import os
#防止出现乱码
plt.rcParams['font.sans-serif']=['SimHei']#黑体
plt.rcParams['axes.unicode_minus'] = False 

def Task_One():
    fn=input('请输入文件名17.tmdb_5000_movies.csv：')
    try:
        df=pd.read_csv(fn)
        print(df.head(3))
        print(df.tail(2))
        print('任务一完成')
    except:
        print('读取文件出错')
def Task_Two():
     fn=input('请输入文件名17.tmdb_5000_movies.csv：')
     try:
        df=pd.read_csv(fn)
        df=df.dropna()
        df_select= df.loc[:, ['budget','id','original_language','release_date','popularity','title']]
        df_select.to_csv('tmdb_5000_movies_budgt_popularity.csv',index=False)
        print('任务二完成')
     except:
        print('读取文件出错')
def Task_Three():
     fn=input('请输入文件名tmdb_5000_movies_budgt_popularity.csv：')
     try:
        df=pd.read_csv(fn)
        df_one = df[df['original_language']== 'en']
        df_one.to_csv('tmdb_5000_movies_budgt_popularity_en.txt',index=False)
        print('任务三完成')
     except:
        print('读取文件出错')
def Task_Four():
     fn=input('请输入文件名tmdb_5000_movies_budgt_popularity_en.txt：')
     try:
        df=pd.read_csv(fn)
        df.to_excel('tmdb_5000_movies_budgt_popularity_en.xlsx',index=False)
        print('任务四完成')
     except:
        print('读取文件出错')   
def Task_Five():
     fn=input('请输入文件名tmdb_5000_movies_budgt_popularity_en.txt：')
     try:
         df5 = pd.read_csv(fn)
         df5['release_date'] = pd.to_datetime(df5['release_date'])
         df6 = df5.set_index('release_date')
         df7 = df6['2000-01-01':'2010-12-31']
         dff = df7.sort_values(by='title',ascending=True)
         for name,color,s in zip(['budget','popularity'],'rg',['movies_en_budget_2000_2010.png','movies_en_popularity_2000_2010.png']):
             X = dff['title'].values.tolist()
             Y = dff[name].values.tolist()
             plt.figure(figsize=(50,5))
             plt.plot(range(len(X)),Y,color=color)
             #添加刻度标签
             plt.xticks(range(0,len(X),50),[X[i] for i in range(0,len(X),50)],rotation=45)
             plt.savefig(s,dpi=400)
             print('任务五完成')
     except:
        print('读取文件出错')           
#系统主界面
def menu():
    print('[任务选择]\n'
           '+——————2000-2010年英语电影预算与受欢迎程度数据分析————————+\n'
           '|0、退出                                    |\n'
           '|1、数据读取                        |\n'
           '|2、数据切片和预处理                                 |\n'
           '|3、数据选择                                |\n'
           '|4、文件类型转换                               |\n'
           '|5、数据可视化                              |\n'
           '+—————————————————————————————————————————————+')
#功能选择模块
def task():
    while True:
        menu()    #打印主界面
        num=input('请输入任务选项:')
        if num=='1':
            Task_One()
        elif num == '2':
            if os.path.exists('17.tmdb_5000_movies.csv'):
                Task_Two()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '3':
            if os.path.exists('tmdb_5000_movies_budgt_popularity.csv'):
                Task_Three()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '4':
            if os.path.exists('tmdb_5000_movies_budgt_popularity_en.txt'):
                Task_Four()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '5':
            if os.path.exists('tmdb_5000_movies_budgt_popularity_en.txt'):
                Task_Five()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num=='0':
            print('程序结束')
            break
        else:
            print('输入选项有误')
        input('回车显示菜单')
#主函数
if __name__ == '__main__' :
    task()     #调用功能选择函数