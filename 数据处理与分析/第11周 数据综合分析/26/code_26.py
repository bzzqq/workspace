# -*- coding: utf-8 -*-
#错误：未指定编码

import pandas as pd
import matplotlib.pyplot as plt
import os

# 防止中文出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']   # 黑体
plt.rcParams['axes.unicode_minus'] = False

#[任务一]
def dataprocessing():
        try:
            filename=input('请输入要打开的文件名26.bike_day.csv:') #指定路径
            df=pd.read_csv(filename)  #读取文件
            print(df.head(5))  #查看前五行
            print(df.tail(2))  #查看后两行          
            df.to_csv('bike_day.csv',sep=' ',index=False)
            print('任务1执行成功！')
        except:  #打开文件失败时候执行的代码
            print('任务1执行失败')
#[任务二]
def  dataselection():
        try:
            filename=input('请输入要打开的文件名bike_day.csv:') #指定路径
            df=pd.read_csv(filename,sep=' ')  
            df=df.dropna()
            df_new=df.loc[:,['instant','dteday','yr','casual','registered']]
            df_new.to_csv('bike_day_user.txt',sep=' ',index=False)
            print('任务2执行成功！')
        except:
            print('任务2执行失败')
#[任务3]
def datacalculate():  
        filename = input('请输入要打开的文件名bike_day_user.txt:')  # 读取数据
        try:
            df_new = pd.read_csv(filename, encoding='cp936',sep=' ')  
            df_new['cnt'] = df_new['casual'] + df_new['registered']  
            df_new.to_excel('bike_day_user_cnt.xlsx',index=False)  
            print('任务3执行成功！')
        except:
            print('任务3执行失败')
#[任务4]
def datadescribe(): 
        filename = input('请输入要打开的文件名bike_day_user_cnt.xlsx:')  # 读取数据
        try:
            df_new = pd.read_excel(filename)  # 读文件
            df_new_max = df_new['cnt'].max()  # 求cnt列最大值
            df_new_min = df_new['cnt'].min()  # 求cnt列最小值
            print('cnt的最大值和最小值为：', df_new_max, df_new_min)
            
            df_new_mean1 = df_new.loc[:, ['yr', 'cnt']] 
            df_new_mnth = df_new.loc[:, ['dteday', 'cnt']]  
            df_new_mean1_groupby = df_new_mean1.groupby(['yr'], as_index=False).sum()
            temp=df_new_mean1_groupby['cnt'].sum()/2
            print('2011和2012年的年平均为：',temp)
            
            df_new_mnth['mnth'] = df_new_mnth['dteday'].map(lambda x: int(x[5:x.rindex('/')]))  
            df_new_mnth_groupby = df_new_mnth.groupby(['mnth'], as_index=False).mean()  
            df_new_mnth_groupby.sort_values('mnth')  
            print('月平均为：', df_new_mnth_groupby)
            df_new_mnth_groupby.to_csv('group.csv', index=False,sep=' ')
            print('任务4执行成功！')
        except:
            print('文件名不存在，请重新输入文件名：')
#[任务5]
def datavisualization():  # 数据可视化
        fileName = input('请输入要打开的文件名group.csv:')  # 读取数据
        try:
            df_new = pd.read_csv(fileName, encoding='cp936',sep=' ')  
            plt.figure(figsize=(12, 8))  # 作图的大小
            x = df_new['cnt']  
            names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                     'November', 'December']  
            plt.barh(range(12), x, color='blue',label='cnt')  
            plt.yticks(range(12), names) 
            plt.title('共享单车租赁用户的月平均值分布图', fontproperties='SimHei', fontsize=14) 
            plt.xlabel('X-月平均值', fontproperties='SimHei', fontsize=14)  # x轴标题、字体、大小
            plt.ylabel('Y-月份', fontproperties='SimHei', fontsize=14)  # y轴标题、字体、大小
            for i in range(12):
                plt.text(int(x[i]), i, int(x[i]))  # 用循环将月平均值标识在柱状图后
            plt.legend()
            plt.savefig('bike_day_user_cnt.png', dpi=300)  
            plt.show()  
            print('任务5执行成功！')
        except:
            print('任务5执行失败')

###############################################################
# 系统主界面
def menu():
    print('[任务选择]\n'
          '+------共享单车租赁用户数据分析及可视化系统------+\n'
          '|0、退出。                                   |\n'
          '|1、数据读取。                         |\n'
          '|2、数据预处理并选择及导出。                           |\n'
          '|3、数据计算。                                |\n'
          '|4、数据统计。                                |\n'
          '|5、数据可视化。                              |\n'
          '+--------------------------------------------+')
# 功能选择模块
def task():
    while True:
        menu()  # 打印系统主界面
        num = input("请输入任务选项：")
        if num == '1':
            dataprocessing()
        elif num == '2':
            if os.path.exists('bike_day.csv'):
                dataselection()
            else:
                print("未能实行当前选项，请先执行前面的选项！")
        elif num == '3':
            if os.path.exists('bike_day_user.txt'):
                datacalculate()
            else:
                print("未能实行当前选项，请先执行前面的选项！")
        elif num == '4':
            if os.path.exists('bike_day_user_cnt.xlsx'):
                datadescribe()
            else:
                print("未能实行当前选项，请先执行前面的选项！")
        elif num == '5':
            if os.path.exists('group.csv'):
                datavisualization()
            else:
                print("未能实行当前选项，请先执行前面的选项！")
        elif num == '0':
            print("程序结束!")
            break
        else:
            print("输入选项有误")
        input("回车显示菜单")

# 主函数
if __name__ == '__main__':
    task()  # 调用功能选择函数
