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
        fn = input('请输入所要打开的文件名称32.house.sale.price.csv:')
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
        fn = input('请输入所要打开的文件名称32.house.sale.price.csv:')
        try:
            df = pd.read_csv(fn)
            df = df.dropna()#丢弃缺失值
            df_Selection = df.loc[:,['Id','LotShape','LotArea','OverallCond','YrSold','SalePrice']]
            try:
                df_Selection.to_csv('house_total_price.txt',index=False,sep=' ') #以空格为数据间的分隔符
                print('任务二执行完成！')
            except:         #若新文件导出失败时执行的代码
                print('文件导出失败！')
        except:             #若文件打开失败时执行的代码
            print('任务二执行失败！')

#【任务三】
def dataExtraction():
        #读取数据
        fn = input('请输入所要打开的文件名称house_total_price.txt:')
        try:
            df = pd.read_csv(fn,sep=' ') #读取时以空格为分隔符
            df['unitPrice'] = (df['SalePrice'] / df['LotArea']) #直接生成新列‘cnt’，其值为该两列数据之和
            df.to_excel('house_unit_price.xlsx',index=False)
            print('任务三执行完成！')
        except:             #若文件打开失败时执行的代码        
            print('任务三执行失败！')
            
#【任务四】
def dataVisualization_1():
        #读取数据
        fn = input('请输入所要打开的文件名称house_unit_price.xlsx:')
        try:
            df = pd.read_excel(fn)
            df_LotShape = df.loc[:,['LotShape','unitPrice']]
            df_LotShape = df_LotShape.groupby(by='LotShape',as_index=False).mean()
            df_LotShape = df_LotShape.sort_values(by='unitPrice',axis=0,ascending=False) #对每平方米售价进行降序排列
            df_LotShape.plot(x='LotShape',kind='bar',figsize=(12,8),grid=0.1) #作柱状图
            plt.title('2006-2010年不同房屋形状的房屋每平方米售价统计图') #命名标题
            plt.xlabel('房屋形状') #设置横轴标签
            plt.ylabel('每平方米的价格') #设置纵轴标签
            plt.savefig('houseshape_unit_price.png',dpi=400) #保存图片
            plt.show()
            print('任务四执行完成！')
        except:             #若文件打开失败时执行的代码
            print('任务四执行失败！')

#【任务五】
def dataVisualization_2():
        #读取数据
        fn = input('请输入所要打开的文件名称house_unit_price.xlsx:')
        try:
            df = pd.read_excel(fn)
            df_LotShape = df.loc[:,['LotShape','OverallCond']]
            df_LotShape = df_LotShape.groupby(by='LotShape',as_index=False).mean()
            df_LotShape = df_LotShape.sort_values(by='OverallCond',axis=0) #对房屋整体状况进行升序排列
            df_LotShape.plot(x='LotShape',kind='bar',figsize=(12,8),grid=0.1) #作柱状图
            plt.title('2006-2010年不同房屋形状的房屋整体状况统计图') #命名标题
            plt.xlabel('房屋形状') #设置横轴标签
            plt.ylabel('房屋整体状况') #设置纵轴标签
            plt.savefig('houseshape_overallcond.png',dpi=400) #保存图片
            plt.show()
            print('任务五执行完成！')
        except:             #若文件打开失败时执行的代码
            print('任务五执行失败！')

#系统主界面
def menu():
    print('                             【任务选择】\n'
          '—————————————2006-2010年不同类型房屋售价数据分析及可视化系统————————————\n'
          '|0.退出数据处理系统                                                   |\n'
          '|1.数据读取                                                   |\n'
          '|2.数据的预处理并挑取及导出                                                   |\n'
          '|3.归纳每平方米售价                                                   |\n'
          '|4.按房屋形状对每平方米售价分类及可视化                                |\n'
          '|5.按房屋形状对房屋整体状况分类及可视化                                |\n'
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
            if os.path.exists('house_total_price.txt'):
                dataExtraction()
            else:
                print('当前不能执行该任务，请先确定是否已执行前面的任务！')
        elif num == '4':
            if os.path.exists('house_unit_price.xlsx'):
                dataVisualization_1()
            else:
                print('当前不能执行该任务，请先确定是否已执行前面的任务！')
        elif num == '5':
            if os.path.exists('house_unit_price.xlsx'):
                dataVisualization_2()
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
