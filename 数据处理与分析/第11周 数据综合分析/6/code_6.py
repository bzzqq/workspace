import pandas as pd
import matplotlib.pyplot as plt
import os

# 防止中文出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False


# 任务【1】
def datapreprocessing():
        filename = input('请输入要打开的文件名6.PRSA_data_2010.1.1-2014.12.31.csv:')  # 打开文件
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读取数据
            print(df.head(3))  # 查看前三行内容
            print(df.tail(2))  # 查看后两行内容
            print('任务1执行成功！')
        except:  # 任务执行不成功时输出的代码
            print('任务1执行不成功，请重新输入！')


# 任务【2】
def dataconduction():
        filename = input('请输入要打开的文件名6.PRSA_data_2010.1.1-2014.12.31.csv:')  # 打开文件
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读取数据
            df = df.dropna()
            df.drop(columns=['DEWP', 'TEMP', 'PRES', 'cbwd', 'Iws', 'Is', 'Ir'], axis=1, inplace=True)
            df.to_csv('6.pm25_data_2010.1.1-2014.12.31.csv', encoding='cp936', index=False)
            print("任务2执行成功！")
        except:
            print("任务2执行不成功，请重新输入！")


# 任务【3】
def dataselection():
        filename = input('请输入要打开的文件名6.pm25_data_2010.1.1-2014.12.31.csv:')
        try:
            df = pd.read_csv(filename, encoding='cp936')
            df_new = df[df['pm2.5'] > 300]
            try:
                df_new.to_csv('6.pm25_hazardous_data_2010.1.1-2014.12.31.txt', encoding='cp936', index=False)
                print("任务3执行成功！")
            except:
                print("任务3执行失败！")
        except:
            print("任务3执行失败！")


# 任务【4】
def datainventory():
    filename = input('请输入要打开的文件名6.pm25_hazardous_data_2010.1.1-2014.12.31.txt：')
    try:
        df = pd.read_csv(filename, encoding='cp936')
        df.to_excel('6.pm25_hazardous_data_2010.1.1-2014.12.31.xlsx', encoding='cp936', index=False)
        print("任务4执行成功！")
    except:
        print("任务4执行失败，请重试！")


# 任务【5】
def datavisualization():
    filename = input('请输入要打开的文件名6.pm25_hazardous_data_2010.1.1-2014.12.31.txt：')
    try:
        df = pd.read_csv(filename, encoding='cp936')
        month_counts = df['month'].value_counts()
        day_counts = df['day'].value_counts()
        hour_counts = df['hour'].value_counts()
        names = ['month', 'day', 'hour']
        x = [1, 2, 3]
        y = [month_counts.max(), day_counts.max(), hour_counts.max()]
        plt.bar(x, y, color=['red', 'green', 'blue'])
        plt.xticks(x, names)
        plt.ylabel('最大频次值', fontproperties='SimHei', fontsize=14)
        plt.title('最大频次柱状图', fontproperties='SimHei', fontsize=14)  # 标题、字体、大小
        plt.savefig('6.pm25_hazardous_month_data_hour.png', dpi=300)  # 保存图表，分辨率为300dpi
        plt.show()  # 展示图表
        print('任务5执行成功！')
    except:
        print('任务5执行失败！')



# 系统主界面
def menu():
    print('[任务选择]\n'
          '+-----2010-2014年北京市PM2.5数据分析及可视化系统----+\n'
          '|0、退出。                                        |\n'
          '|1、数据读取。                              |\n'
          '|2、数据预处理及导出。                                |\n'
          '|3、数据选择及导出。                                |\n'
          '|4、数据转存。                                     |\n'
          '|5、数据可视化。                                   |\n'
          '+--------------------------------------------------+')


# 功能选择模块
def task():
    while True:
        menu()  # 打印系统主界面
        num = input("请输入任务选项：")
        if num == '1':
            datapreprocessing()
        elif num == '2':
            if os.path.exists('6.PRSA_data_2010.1.1-2014.12.31.csv'):
                dataconduction()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '3':
            if os.path.exists('6.pm25_data_2010.1.1-2014.12.31.csv'):
                dataselection()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '4':
            if os.path.exists('6.pm25_hazardous_data_2010.1.1-2014.12.31.txt'):
                datainventory()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '5':
            if os.path.exists('6.pm25_hazardous_data_2010.1.1-2014.12.31.txt'):
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