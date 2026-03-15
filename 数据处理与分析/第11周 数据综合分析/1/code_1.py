import pandas as pd
import matplotlib.pyplot as plt
import os

# 防止中文出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']   # 黑体
plt.rcParams['axes.unicode_minus'] = False

# 任务【1】
def datapreprocessing():  # 加工数据
        filename = input('请输入要打开的文件名1.pollution_us_5city_2010_SO2_O3_NO2_CO.csv:')  # 打开文件
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读取数据
            print(df.head(3))  # 查看前三行内容
            print(df.tail(2))  # 查看后两行内容
            print('任务1执行成功！')
        except:  # 任务执行不成功时输出的代码
            print('任务1执行不成功，请重新输入！')

# 任务【2】
def dataconduction():  # 处理数据
        filename = input('请输入要打开的文件名1.pollution_us_5city_2010_SO2_O3_NO2_CO.csv：')  # 打开文件
        try:
            df1 = pd.read_csv(filename, encoding='cp936')  # 读取数据
            df1 = df1.dropna()  # 丢弃缺失值
            df1.drop(['State Code', 'County Code', 'Site Num', 'Address'], axis=1, inplace=True)
            df1.to_csv('pollution_us_5city_2010_SO2_O3_NO2_CO_new.csv', encoding='cp936', index=False)
            print("任务2执行成功！")
        except:
            print("任务2执行不成功，请重新输入！")

# 任务【3】
def dataselection():  # 选择数据
        filename = input('请输入要打开的文件名pollution_us_5city_2010_SO2_O3_NO2_CO_new.csv：')
        try:
            df = pd.read_csv(filename, encoding='cp936')
            df1 = df[df['County'] == 'Queens']
            try:
                df1.to_csv('pollution_us_Queens_2010_SO2_O3_NO2_CO_new.txt', encoding='cp936', index=False)
                print("任务3执行成功！")
            except:
                print("任务3执行失败！")
        except:
            print("任务3执行失败！！")

# 任务【4】
def datainventory():  # 转存数据
    filename = input('请输入要打开的文件名pollution_us_Queens_2010_SO2_O3_NO2_CO_new.txt：')
    try:
        df = pd.read_csv(filename, encoding='cp936')
        df.to_excel('pollution_us_Queens_2010_SO2_O3_NO2_CO_new.xlsx', index=False)
        print("任务4执行成功！")
    except:
        print("任务4执行失败")

# 任务【5】
def datavisualization():  # 数据可视化
    filename = input('请输入要打开的文件名pollution_us_Queens_2010_SO2_O3_NO2_CO_new.txt：')
    try:
        df = pd.read_csv(filename, encoding='cp936')
        df['month'] = df['Date Local'].map(lambda x: int(x[5:x.rindex('/')]))   # 选取月份
        df_mean1 = df.loc[:, ['NO2 Mean', 'month']]
        df_mean2 = df.loc[:, ['SO2 Mean', 'month']]
        df_mean3 = df.loc[:, ['O3 Mean', 'month']]
        df_mean4 = df.loc[:, ['CO Mean', 'month']]
        df_mean1_groupby = df_mean1.groupby(['month'], as_index=False).mean()
        df_mean2_groupby = df_mean2.groupby(['month'], as_index=False).mean()
        df_mean3_groupby = df_mean3.groupby(['month'], as_index=False).mean()
        df_mean4_groupby = df_mean4.groupby(['month'], as_index=False).mean()
        df_mean1_groupby.sort_values('month')  # 按照月份从小到大排序
        df_mean2_groupby.sort_values('month')  # 按照月份从小到大排序
        df_mean3_groupby.sort_values('month')  # 按照月份从小到大排序
        df_mean4_groupby.sort_values('month')  # 按照月份从小到大排序
        df_mean1_groupby.to_csv('NO2_mean.csv', index=False)  # 将月平均放到一个新的csv文件中方便作图
        df_mean2_groupby.to_csv('SO2_mean.csv', index=False)  # 将月平均放到一个新的csv文件中方便作图
        df_mean3_groupby.to_csv('O3_mean.csv', index=False)  # 将月平均放到一个新的csv文件中方便作图
        df_mean4_groupby.to_csv('CO_mean.csv', index=False)  # 将月平均放到一个新的csv文件中方便作图
        try:
            df_new = pd.read_csv('NO2_mean.csv', encoding='cp936')  # 读文件
            plt.figure(figsize=(12, 8))  # 作图的大小
            y = df_new['NO2 Mean']
            names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                     'November', 'December']
            plt.plot(range(12), y, color='red', marker='o',label='NO2')
            plt.xticks(range(12), names)
            plt.title('2010年NO2的平均值', fontproperties='SimHei', fontsize=14)
            plt.xlabel('X-月份', fontproperties='SimHei', fontsize=14)
            plt.ylabel('Y-月平均值', fontproperties='SimHei', fontsize=14)
            plt.legend()#错误：未添加图例
            plt.savefig('NO2_Mean.png', dpi=300)
            plt.show()
            
            df_new = pd.read_csv('SO2_mean.csv', encoding='cp936')  # 读文件
            plt.figure(figsize=(12, 8))  # 作图的大小
            y = df_new['SO2 Mean']
            names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                     'November', 'December']
            plt.plot(range(12), y, color='green', marker='o',label='SO2')
            plt.xticks(range(12), names)
            plt.title('2010年SO2的平均值', fontproperties='SimHei', fontsize=14)
            plt.xlabel('X-月份', fontproperties='SimHei', fontsize=14)
            plt.ylabel('Y-月平均值', fontproperties='SimHei', fontsize=14)
            plt.legend()#错误：未添加图例
            plt.savefig('SO2_Mean.png', dpi=300)
            plt.show()
            
            df_new = pd.read_csv('O3_mean.csv', encoding='cp936')  # 读文件
            plt.figure(figsize=(12, 8))  # 作图的大小
            y = df_new['O3 Mean']
            names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                     'November', 'December']
            plt.plot(range(12), y, color='blue', marker='o',label='O3')
            plt.xticks(range(12), names)
            plt.title('2010年O3的平均值', fontproperties='SimHei', fontsize=14)
            plt.xlabel('X-月份', fontproperties='SimHei', fontsize=14)
            plt.ylabel('Y-月平均值', fontproperties='SimHei', fontsize=14)
            plt.legend()#错误：未添加图例
            plt.savefig('O3_Mean.png', dpi=300)
            plt.show()
            
            df_new = pd.read_csv('CO_mean.csv', encoding='cp936')  # 读文件
            plt.figure(figsize=(12, 8))  # 作图的大小
            y = df_new['CO Mean']
            names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                     'November', 'December']
            plt.plot(range(12), y, color='black', marker='o',label='CO')
            plt.xticks(range(12), names)
            plt.title('2010年CO的平均值', fontproperties='SimHei', fontsize=14)
            plt.xlabel('X-月份', fontproperties='SimHei', fontsize=14)
            plt.ylabel('Y-月平均值', fontproperties='SimHei', fontsize=14)
            plt.legend()#错误：未添加图例
            plt.savefig('CO_Mean.png', dpi=300)
            plt.show()
            print('任务5执行成功！')
        except:
            print('任务5执行不成功！')
    except:
        print('任务5执行不成功')


            

# 系统主界面
def menu():
    print('[任务选择]\n'
          '+-----美国五个著名城市空气质量分析及可视化系统----+\n'
          '|0、退出。                                    |\n'
          '|1、数据读取。                          |\n'
          '|2、数据预处理及导出。                            |\n'
          '|3、数据选择及导出。                            |\n'
          '|4、数据转存。                                 |\n'
          '|5、数据可视化。                                |\n'
          '+---------------------------------------------+')

# 功能选择模块
def task():
    while True:
        menu()  # 打印系统主界面
        num = input("请输入任务选项：")
        if num == '1':
            datapreprocessing()
        elif num == '2':
            if os.path.exists('1.pollution_us_5city_2010_SO2_O3_NO2_CO.csv'):
                dataconduction()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '3':
            if os.path.exists('pollution_us_5city_2010_SO2_O3_NO2_CO_new.csv'):
                dataselection()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '4':
            if os.path.exists('pollution_us_Queens_2010_SO2_O3_NO2_CO_new.txt'):
                datainventory()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '5':
            if os.path.exists('pollution_us_Queens_2010_SO2_O3_NO2_CO_new.txt'):
                datavisualization()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '0':
            print('整个程序执行结束！')
            break
        else:
            print("输入的选项有误，请重新输入！")
        input("请回车以显示菜单")

# 主函数
if __name__ == '__main__':
    task()  # 调用功能选择函数