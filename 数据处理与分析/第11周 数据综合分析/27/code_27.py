# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import os

# 防止中文出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False


# [任务一]
def dataprocessing():
        try:
            filename = input('请输入要打开的文件名27.bike_day.csv:')  # 指定路径
            df = pd.read_csv(filename)  # 读取文件
            print(df.head(5))  # 查看前五行
            print(df.tail(2))  # 查看后两行
           
            df.to_csv('bike_day.csv',index=False)
            print('任务1执行成功！')

        except:  # 打开文件失败时候执行的代码
            print('任务1执行失败')


# [任务二]
def dataselection():
        try:
            filename = input('请输入要打开的文件名bike_day.csv:')  # 指定路径
            df = pd.read_csv(filename)  # 读取文件 
            df = df.dropna()
            df_new = df.loc[:, ['instant', 'dteday', 'weekday', 'casual', 'registered']]
            df_new.to_csv('bike_weekday_user.txt',sep=' ',index=False)
            print('任务2执行成功！')
        except:
            print('任务2执行失败')


# [任务3]
def datacalculate():
        filename = input('请输入要打开的文件名bike_weekday_user.txt:')  # 读取数据
        try:
            df_new = pd.read_csv(filename, encoding='cp936',sep=' ') 
            print(df_new)
            df_new['cnt'] = df_new['casual'] + df_new['registered']
            print(df_new)
            df_new.to_excel('bike_weekday_user_cnt.xlsx', index=False)
            print('任务3执行成功！')
        except:
            print('任务3执行失败')


# [任务4]
def datadescribe():
        filename = input('请输入要打开的文件名bike_weekday_user_cnt.xlsx:')  # 读取数据
        try:
            df_new = pd.read_excel(filename)  # 读文件
            print(df_new)
            df_new_groupy = df_new.groupby(['weekday'],as_index=False).mean()
            df_choice = df_new_groupy.loc[:, ['weekday','cnt']]
            df_choice.to_csv('bike_weekday_user_cnt_mean.txt',sep=' ',index=False)
            print('任务4执行成功！')
            #break
        except:
            print('文件名不存在，请重新输入文件名：')


# [任务5]
def datavisualization():  # 数据可视化
        fileName = input('请输入要打开的文件名bike_weekday_user_cnt_mean.txt:')  # 读取数据
        try:
            df_choice = pd.read_csv(fileName, encoding='cp936',sep=' ')  
            df_choice['weekday'] = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            df_choice.plot(kind='bar',
                           x='weekday',
                           title='weekday-cnt',
                           legend=True,
                           color='blue',
                           rot=45)  # 数据可视化
            plt.title('weekday-cnt') #命名标题 
            plt.xlabel('日期') #设置轴标签
            plt.ylabel('cnt') #设置轴标签
            plt.savefig('bike_day_user_cnt.png', dpi=400)
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
            if os.path.exists('bike_weekday_user.txt'):
                datacalculate()
            else:
                print("未能实行当前选项，请先执行前面的选项！")
        elif num == '4':
            if os.path.exists('bike_weekday_user_cnt.xlsx'):
                datadescribe()
            else:
                print("未能实行当前选项，请先执行前面的选项！")
        elif num == '5':
            if os.path.exists('bike_weekday_user_cnt_mean.txt'):
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
