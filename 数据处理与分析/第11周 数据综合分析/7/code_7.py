import pandas as pd
import matplotlib.pyplot as plt
import os

# 防止中文出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False


# 任务【1】
def datapreprocessing():
        filename = input('请输入要打开的文件名7.PRSA_data_2010.1.1-2014.12.31.csv:')  # 打开文件
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读取数据
            print(df.head(3))  # 查看前三行内容
            print(df.tail(2))  # 查看后两行内容
            df.fillna(100, inplace=True)
            df.to_csv('7.PRSA_data_2010.1.1-2014.12.31new.csv', encoding='cp936', index=False)
            print('任务1执行成功！')
        except:  # 任务执行不成功时输出的代码
            print('任务1执行不成功，请重新输入！')


# 任务【2】
def dataconduction():
        filename = input('请输入要打开的文件名7.PRSA_data_2010.1.1-2014.12.31new.csv：')  # 打开文件
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读取数据
            df.drop(columns=['pm2.5', 'DEWP', 'PRES', 'cbwd', 'Iws', 'Is', 'Ir'], axis=1, inplace=True)
            df = df.fillna(100)
            df.to_excel('7.temp_data_2010.1.1-2014.12.31.xlsx', encoding='cp936', index=False)
            print("任务2执行成功！")
        except:
            print("任务2执行不成功，请重新输入！")


# 任务【3】
def dataselection():
        filename = input('请输入要打开的文件名7.temp_data_2010.1.1-2014.12.31.xlsx：')
        try:
            df = pd.read_excel(filename, encoding='cp936')
            df_new = df[df['year'] == 2010]
            try:
                df_new.to_csv('7.temp_data_2010.txt', encoding='cp936', index=False,sep=' ')#错误：未使用空格间隔
                print("任务3执行成功！")
            except:
                print("任务3执行失败！")
        except:
            print("任务3执行失败！")


# 任务【4】
def datainventory():
    filename = input('请输入要打开的文件名7.temp_data_2010.txt：')
    try:
        df = pd.read_csv(filename, encoding='cp936',sep=' ')
        df.to_csv('7.temp_data_2010.csv', encoding='cp936', index=False)
        print("任务4执行成功！")
    except:
        print("任务4执行失败，请重试！")


# 任务【5】
def datavisualization():
    filename = input('请输入要打开的文件名7.temp_data_2010.csv：')
    try:
        df = pd.read_csv(filename, encoding='cp936')
        df_mean = df.loc[:, ['TEMP', 'month']]
        df_mean_groupby = df_mean.groupby(['month'], as_index=False).mean()
        df1 = df_mean_groupby.sort_values(['month'])  # 按照月份从小到大排序
        df1.to_csv('TEMP_Mean.csv', encoding='cp936', index=False)  # 将月平均放到一个新的csv文件中方便作图
        try:
            df_new1 = pd.read_csv('TEMP_Mean.csv', encoding='cp936')  # 读文件
            plt.figure(figsize=(12, 8))  # 作图的大小
            y1 = df_new1['TEMP']
            names1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                      '11', '12']
            plt.plot(range(12), y1, color='red', marker='o',label='TEMP')
            plt.xticks(range(12), names1)
            plt.title('2010年的TEMP月均值', fontproperties='SimHei', fontsize=14)
            plt.xlabel('X-2010年的月份', fontproperties='SimHei', fontsize=14)
            plt.ylabel('Y-月平均值', fontproperties='SimHei', fontsize=14)
            plt.legend()
            plt.savefig('TEMP_Mean.png', dpi=300)
            plt.show()
            print('任务5执行成功！')
        except:
            print("任务5执行失败，请重试！")
    except:
        print('任务5执行失败！')


# 系统主界面
def menu():
    print('[任务选择]\n'
          '+-----2010-2014年北京地面温度数据分析及可视化系统----+\n'
          '|0、退出。                                        |\n'
          '|1、数据读取。                             |\n'
          '|2、数据预处理及导出。                               |\n'
          '|3、数据选择及导出。                               |\n'
          '|4、数据转存。                                    |\n'
          '|5、数据可视化。                                  |\n'
          '+-------------------------------------------------+')


# 功能选择模块
def task():
    while True:
        menu()  # 打印系统主界面
        num = input("请输入任务选项：")
        if num == '1':
            datapreprocessing()
        elif num == '2':
            if os.path.exists('7.PRSA_data_2010.1.1-2014.12.31new.csv'):
                dataconduction()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '3':
            if os.path.exists('7.temp_data_2010.1.1-2014.12.31.xlsx'):
                dataselection()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '4':
            if os.path.exists('7.temp_data_2010.txt'):
                datainventory()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '5':
            if os.path.exists('7.temp_data_2010.csv'):
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