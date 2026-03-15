# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import os
#防止出现乱码
plt.rcParams['font.sans-serif']=['SimHei']#黑体
plt.rcParams['axes.unicode_minus'] = False 

def Task_One():
    fn=input('请输入文件名12.nino3.long.anom.data.csv：')
    try:

        df = pd.read_csv(fn)
        with open('nino3_dropnan.txt','w') as fp:
            fp.write('Date,Nino3\n')
            counts=df['Year'].value_counts()
            for year in range(len(counts)):#                
                y = str(df.iloc[year,0])
                for month in range(1,13):
                    m = str(month).rjust(2,'0')
                    Nino3 = str(df.iloc[year,month])
                    s = y+'-'+m+'-01'+','+Nino3+'\n'
                    fp.write(s)
        df1 = pd.read_csv('nino3_dropnan.txt')
        df2 = df1.dropna()
        df2.to_csv('nino3_dropnan.txt',index=False)
        print('任务一完成')            
    except:
        print('读取文件出错')
def Task_Two():
     fn=input('请输入文件名nino3_dropnan.txt：')
     try:
        df=pd.read_csv(fn)        
        df_describe = df.describe()
        maxValue = df_describe.at['max','Nino3']
        minValue = df_describe.at['min','Nino3']
        meanValue = df_describe.at['mean','Nino3']
        print('最大值是：'+str(maxValue))
        print('最小值是：'+str(minValue))
        print('平均值是：'+str(meanValue))
        print('任务二完成')
     except:
        print('读取文件出错')
def Task_Three():
     fn=input('请输入文件名nino3_dropnan.txt：')
     try:
        df=pd.read_csv(fn)        
        df_describe = df.describe()
        maxValue = df_describe.at['max','Nino3']
        minValue = df_describe.at['min','Nino3']
        category = [minValue, -0.5, 0,0.5,maxValue]
        labels =['LaNinaTemp', 'Cold', 'Warm', 'NinoTemp']
        x = pd.cut(df['Nino3'],category,right=False,labels=labels).rename('Label')
        df4 = pd.concat([df,x],axis=1)
        df4.to_csv('nino3_dropnan_result.csv',index=False)

        plt.figure()
        plt.pie([i[1] for i in list(x.value_counts().items())],
        labels=labels)

        plt.savefig('nino3_ pie.png',dpi=300)
        plt.show()
        
        print('任务三完成')
     except:
        print('读取文件出错')
def Task_Four():
     fn=input('请输入文件名nino3_dropnan_result.csv：')
     try:
         df3 = pd.read_csv(fn)
         import itertools
         mylist = df3['Label'].values.tolist()
         num_times = [(k, len(list(v))) for k, v in itertools.groupby(mylist)]
         #print(num_times)

         result=[]
         for name in ['NinoTemp','LaNinaTemp']:
            index=[]
            begins=[]
            for i in range(len(num_times)):
                if num_times[i][0]==name and num_times[i][1]>5:
                    index.append(i)
            x = [i[1] for i in num_times]
            for i in index:
                begin = sum(x[:i])
                begins.append(begin)
            result.append(df3.iloc[begins,:]['Date'].values.tolist())
         LaNinaList = [i+'\n' for i in result[1]]
         NinoList = [i+'\n' for i in result[0]]

         with open('LaNinaStartDate.txt','w') as fp:
            fp.writelines(LaNinaList)
         with open('NinoStartDate.txt','w') as fp:
            fp.writelines(NinoList)
         print('任务四完成')
     except:
        print('读取文件出错')   
    
#系统主界面
def menu():
    print('[任务选择]\n'
           '+——————1870-2018年Nino3区海平面温度异常分析————————+\n'
           '|0、退出                                    |\n'
           '|1、数据读取和预处理                         |\n'
           '|2、数据最值计算                               |\n'
           '|3、数据分类并可视化                                |\n'
           '|4、数据统计                              |\n'          
           '+—————————————————————————————————————————————+')
#功能选择模块
def task():
    while True:
        menu()    #打印主界面
        num=input('请输入任务选项:')
        if num=='1':
            Task_One()
        elif num == '2':
            if os.path.exists('nino3_dropnan.txt'):
                Task_Two()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '3':
            if os.path.exists('nino3_dropnan.txt'):
                Task_Three()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '4':
            if os.path.exists('nino3_dropnan_result.csv'):
                Task_Four()
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