# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import os
#防止出现乱码
plt.rcParams['font.sans-serif']=['SimHei']#黑体
plt.rcParams['axes.unicode_minus'] = False 

def Task_One():
    fn=input('请输入文件名18.tmdb_5000_movies.csv：')
    try:
        df=pd.read_csv(fn)
        print(df.head(3))
        print(df.tail(2))
        print('任务一完成')
    except:
        print('读取文件出错')
def Task_Two():
     fn=input('请输入文件名18.tmdb_5000_movies.csv：')
     try:
        df=pd.read_csv(fn)
        df=df.dropna()
        df_select= df.loc[:, ['id','release_date','title','vote_average','vote_count']]
        df_select.to_csv('tmdb_5000_movies_vote.csv',index=False)
        print('任务二完成')
     except:
        print('读取文件出错')
def Task_Three():
     fn=input('请输入文件名tmdb_5000_movies_vote.csv：')
     try:
        df=pd.read_csv(fn)
        df1=df.sort_values(by='vote_average', ascending=False)#错误：文件导出时，未将排序文件导出
        df1.to_csv('tmdb_5000_movies_vote_descending.txt',index=False)
        print('任务三完成')
     except:
        print('读取文件出错')
def Task_Four():
     fn=input('请输入文件名tmdb_5000_movies_vote_descending.txt：')
     try:
        df=pd.read_csv(fn)
        print('最大值：',df['vote_average'].max())
        print('最小值：',df['vote_average'].min())
        print('平均值：',df['vote_average'].mean())
        print('任务四完成')
     except:
        print('读取文件出错')   
def Task_Five():
     fn=input('请输入文件名tmdb_5000_movies_vote_descending.txt：')
     try:
        df=pd.read_csv(fn)
        maxValue=df['vote_average'].max()
        minValue=df['vote_average'].min()
        category=[minValue,5,7,8,maxValue]
        labels = ['bad','ok','good','excellent']
        df['Label']=pd.cut(df['vote_average'],category,labels=labels,right=False)
        df.to_csv('tmdb_5000_movies_vote_descending_result.csv',index=False)       
        df_cLabel=df['Label'].value_counts()
        plt.figure()
        df_cLabel.plot(kind='pie',
                     x='Label',
                     title='presidential_polls_trump_state_support',
                     legend=True)
        plt.savefig('tmdb_5000_movies_vote_descending_result_ pie.png',dpi=300)
        plt.show()
        print('任务五完成')
     except:
        print('读取文件出错')           
#系统主界面
def menu():
    print('[任务选择]\n'
           '+——————2000-2015年电影评分数据分析————————+\n'
           '|0、退出                                    |\n'
           '|1、数据读取                        |\n'
           '|2、数据切片和预处理                                 |\n'
           '|3、数据排序                                |\n'
           '|4、数据特征值计算                              |\n'
           '|5、数据分类和可视化                                |\n'
           '+—————————————————————————————————————————————+')
#功能选择模块
def task():
    while True:
        menu()    #打印主界面
        num=input('请输入任务选项:')
        if num=='1':
            Task_One()
        elif num == '2':
            if os.path.exists('18.tmdb_5000_movies.csv'):
                Task_Two()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '3':
            if os.path.exists('tmdb_5000_movies_vote.csv'):
                Task_Three()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '4':
            if os.path.exists('tmdb_5000_movies_vote_descending.txt'):
                Task_Four()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '5':
            if os.path.exists('tmdb_5000_movies_vote_descending.txt'):
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