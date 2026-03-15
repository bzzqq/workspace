import pandas as pd
import matplotlib.pyplot as plt
import os

# 防止中文出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False


# 任务【1】
def datapreprocessing():
        filename = input('请输入要打开的文件名5.pollution_us_5city_2006_2010_CO.csv:')  # 打开文件
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读取数据
            df = df.dropna()  # 丢弃缺失值
            print(df.head(5))  # 查看前三行内容
            print(df.tail(2))  # 查看后两行内容
            print('任务1执行成功！')
        except:  # 任务执行不成功时输出的代码
            print('任务1执行不成功，请重新输入！')


# 任务【2】
def dataconduction():
        filename = input('请输入要打开的文件名5.pollution_us_5city_2006_2010_CO.csv：')  # 打开文件
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读取数据
            df_new = df[df['City'] == 'New York']
            df1 = df_new.loc[:, ['City', 'Date Local', 'CO Mean', 'CO 1st Max Hour']]
            df1.to_csv('pollution_us_NewYork_2006_2010_COMean.txt', encoding='cp936',sep=' ', index=False)#错误：未使用空格间隔
            print("任务2执行成功！")
        except:
            print("任务2执行不成功，请重新输入！")


# 任务【3】
def dataselection():
        filename = input('请输入要打开的文件名pollution_us_NewYork_2006_2010_COMean.txt：')
        try:
            df = pd.read_csv(filename, encoding='cp936',sep=' ')
            df_new = df[df['CO 1st Max Hour'] == 20]

            try:
                plt.figure(figsize=(12, 8))  # 作图的大小

                df_new1 = df_new.groupby('Date Local', as_index=False).mean()
                df_new1['date'] = pd.to_datetime(df_new1['Date Local'], format="%Y-%m-%d")

                df_new2 = df_new1.sort_values('date')
                print(df_new2)              
                xlength = len(df_new2)
                xticksloc = [i for i in range(xlength) if i %20 == 0]
                print('xticksloc=', xticksloc)
                xtickslabels = df_new2['Date Local'].values[::20]
                print('xtickslabels=', xtickslabels)                

                y = df_new2['CO Mean']               

                plt.xticks(xticksloc, xtickslabels,rotation=45)
                plt.plot(list(y.values), color='red')
                plt.xlabel('Date Local', fontproperties='SimHei', fontsize=14)
                plt.ylabel('CO Mean值', fontproperties='SimHei', fontsize=14)
                plt.title('CO Mean值', fontproperties='SimHei', fontsize=14)
                plt.show()
                print("任务3执行成功！")
            except:
                print("任务3执行失败！")
        except:
            print("任务3执行失败！")


# 任务【4】
def datainventory():
    filename = input('请输入要打开的文件名5.pollution_us_5city_2006_2010_CO.csv：')
    try:
        df = pd.read_csv(filename, encoding='cp936')
        df_new = df[df['City'] == 'New York']
        df1 = df_new.loc[:, ['City', 'Date Local', 'CO AQI']]
        df1 = df1.dropna()  # 丢弃缺失值
        df1 = df1.drop_duplicates()  # 去除重复数据
        df1['CO AQI'] = df1['CO AQI'].map(lambda x: int(x))
        df2 = df1.sort_values(by=['CO AQI'], ascending=False)
        df2.to_excel('pollution_us_NewYork_2006_2010_COAQL.xlsx', encoding='cp936', index=False)
        print("任务4执行成功！")
    except:
        print("任务4执行失败，请重试！")


# 任务【5】
def datavisualization():
    filename = input('请输入要打开的文件名pollution_us_NewYork_2006_2010_COAQL.xlsx：')
    try:
        df = pd.read_excel(filename, encoding='cp936')
        data = df['CO AQI']
        category = [0, 2, 4, 14, 24, 36, 48]
        labels = ['Good', 'Moderate', 'SubUnhealthy', 'Unhealthy', 'VeryUnhealthy', 'Hazardous']
        data_cut = pd.cut(data, category, right=False, labels=labels)
        data_cut_counts = data_cut.value_counts()
        plt.figure()
        data_cut_counts.plot(kind='pie', autopct='%1.1f%%', figsize=(12, 8))
        plt.title('CO AQI离散化统计饼状图', fontproperties='SimHei', fontsize=14)  # 标题、字体、大小
        plt.savefig('CO_AQI_pie.png', dpi=300)  # 保存图表，分辨率为300dpi
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
          '|2、数据预处理及导出。                            |\n'
          '|3、数据选择及画图。                            |\n'
          '|4、数据排序与转存。                             |\n'
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
            if os.path.exists('5.pollution_us_5city_2006_2010_CO.csv'):
                dataconduction()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '3':
            if os.path.exists('pollution_us_NewYork_2006_2010_COMean.txt'):
                dataselection()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '4':
            if os.path.exists('5.pollution_us_5city_2006_2010_CO.csv'):
                datainventory()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '5':
            if os.path.exists('pollution_us_NewYork_2006_2010_COAQL.xlsx'):
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
