import pandas as pd
import matplotlib.pyplot as plt
import os

# 防止中文出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False


# 任务【1】
def datapreprocessing():
        filename = input('请输入要打开的文件名4.pollution_us_5city_2006_2010_NO2.csv:')  # 打开文件
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读取数据
            print(df.head(5))  # 查看前五行内容
            print(df.tail(2))  # 查看后两行内容
            print('任务1执行成功！')
        except:  # 任务执行不成功时输出的代码
            print('任务1执行不成功！')


# 任务【2】
def dataselection():
        filename = input('请输入要打开的文件名4.pollution_us_5city_2006_2010_NO2.csv：')  # 打开文件
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读取数据
            df['year'] = df['Date Local'].map(lambda x: int(x[0:x.index('/')]))
            df1 = df[df['year'] == 2007]
            df1.to_csv('pollution_us_5city_2007_NO2.txt', encoding='cp936', index=False,sep=' ')#错误：未使用空格间隔
            print("任务2执行成功！")
        except:
            print("任务2执行不成功！")


# 任务【3】
def dataconduction():
    filename = input('请输入要打开的文件名pollution_us_5city_2007_NO2.txt：')
    try:
        df = pd.read_csv(filename, encoding='cp936',sep=' ')
        print('总行数：', len(df.index))
        print('总列数：', len(df.columns))
        df1 = df.sort_values(by=['County Code'], ascending=False)  # 按照月份从小到大排序
        df1.to_csv('pollution_us_5city_2007_NO2_descending.csv', encoding='cp936', index=False)
        print("任务4执行成功！")
    except:
        print("任务4执行失败，请重试！")


# 任务【4】
def datavisualization():
    filename = input('请输入要打开的文件名pollution_us_5city_2007_NO2_descending.csv：')
    try:
        df = pd.read_csv(filename, encoding='cp936')
        df_new = df[df['County'] == 'Queens']
        data = df_new['NO2 AQI']
        category = [0, 20, 40, 80, 100, 140, 180]
        labels = ['Good', 'Moderate', 'SubUnhealthy', 'Unhealthy', 'VeryUnhealthy', 'Hazardous']
        data_cut = pd.cut(data, category, right=False, labels=labels)
        data_cut_counts = data_cut.value_counts()
        print(data_cut_counts)
        plt.figure()
        data_cut_counts.plot(kind='bar',  figsize=(12, 8))
        plt.title('NO2 AQI离散化统计柱状图', fontproperties='SimHei', fontsize=14)  # 标题、字体、大小
        plt.savefig('NO2 AQI_bar.png', dpi=300)  # 保存图表，分辨率为300dpi
        plt.show()  # 展示图表
        data_cut_counts.plot(kind='pie', autopct='%1.1f%%', figsize=(12, 8))
        plt.title('NO2 AQI离散化统计饼状图', fontproperties='SimHei', fontsize=14)  # 标题、字体、大小
        plt.savefig('NO2 AQI_pie.png', dpi=300)  # 保存图表，分辨率为300dpi
        plt.show()  # 展示图表
        print('任务5执行成功！')
    except:
        print('任务5执行失败！')


# 系统主界面
def menu():
    print('[任务选择]\n'
          '+-----美国五个著名城市空气质量分析及可视化系统----+\n'
          '|0、退出。                                    |\n'
          '|1、数据读取。                          |\n'
          '|2、数据预处理并选择及导出。                            |\n'
          '|3、数据处理及导出。                             |\n'
          '|4、数据可视化。                                |\n'
          '+---------------------------------------------+')


# 功能选择模块
def task():
    while True:
        menu()  # 打印系统主界面
        num = input("请输入任务选项：")
        if num == '1':
            datapreprocessing()
        elif num == '2':
            if os.path.exists('4.pollution_us_5city_2006_2010_NO2.csv'):
                dataselection()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '3':
            if os.path.exists('pollution_us_5city_2007_NO2.txt'):
                dataconduction()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '4':
            if os.path.exists('pollution_us_5city_2007_NO2_descending.csv'):
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