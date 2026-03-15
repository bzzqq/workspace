import pandas as pd
import matplotlib.pyplot as plt
import os


# 防止中文出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False


# 任务【1】
def datapreprocessing():
        filename = input('请输入要打开的文件名3.pollution_us_5city_2006_2010_O3.csv:')  # 打开文件
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读取数据
            print(df.head(5))  # 查看前五行内容
            print(df.tail(2))  # 查看后两行内容
            print('任务1执行成功！')
        except:  # 任务执行不成功时输出的代码
            print('任务1执行不成功！')

# 任务【2】
def dataconduction():
        filename = input('请输入要打开的文件名3.pollution_us_5city_2006_2010_O3.csv：')  # 打开文件
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读取数据
            df1 = df.dropna()  # 丢弃缺失值
            df1.drop(['ID'], axis=1, inplace=True)
            df2 = df1.drop_duplicates()
            df2.to_csv('pollution_us_5city_2007_2009_O3.csv', encoding='cp936', index=False)
            print("任务2执行成功！")
        except:
            print("任务2执行不成功！")


# 任务【3】
def dataselection():
        filename = input('请输入要打开的文件名pollution_us_5city_2007_2009_O3.csv：')
        try:
            df = pd.read_csv(filename, encoding='cp936')
            df_new1 = df[df['City'] == 'Houston']
            df_new2 = df[df['City'] == 'New York']
            df_new3 = df[df['City'] == 'Washington']
            try:
                df_new1.to_csv('pollution_us_Houston_2007_2009_O3.txt', encoding='cp936', index=False,sep=' ')#错误：未使用空格间隔
                df_new2.to_csv('pollution_us_NewYork_2007_2009_O3.txt', encoding='cp936', index=False,sep=' ')#错误：未使用空格间隔
                df_new3.to_csv('pollution_us_Washington_2007_2009_O3.txt', encoding='cp936', index=False,sep=' ')#错误：未使用空格间隔
                print("任务3执行成功！")
            except:
                print("任务3执行失败！")
        except:
            print("任务3执行失败！")


# 任务【4】
def datainventory():
    filename1 = input('请输入要打开的文件名pollution_us_Houston_2007_2009_O3.txt：')
    filename2 = input('请输入要打开的文件名pollution_us_NewYork_2007_2009_O3.txt：')
    filename3 = input('请输入要打开的文件名pollution_us_Washington_2007_2009_O3.txt：')
    try:
        df1 = pd.read_csv(filename1, encoding='cp936',sep=' ')
        df2 = pd.read_csv(filename2, encoding='cp936',sep=' ')
        df3 = pd.read_csv(filename3, encoding='cp936',sep=' ')
        df1.to_excel('pollution_us_Houston_2007_2009_O3.xlsx',  index=False)
        df2.to_excel('pollution_us_NewYork_2007_2009_O3.xlsx', index=False)
        df3.to_excel('pollution_us_Washington_2007_2009_O3.xlsx', index=False)
        print("任务4执行成功！")
    except:
        print("任务4执行失败！")


# 任务【5】
def datavisualization():
    filename1 = input('请输入要打开的文件名pollution_us_Houston_2007_2009_O3.xlsx：')
    filename2 = input('请输入要打开的文件名pollution_us_NewYork_2007_2009_O3.xlsx：')
    filename3 = input('请输入要打开的文件名pollution_us_Washington_2007_2009_O3.xlsx：')
    try:
        df1 = pd.read_excel(filename1, encoding='cp936')
        df2 = pd.read_excel(filename2, encoding='cp936')
        df3 = pd.read_excel(filename3, encoding='cp936')

        df1['O3 Mean'] = df1['O3 Mean'].map(lambda x: float(x))
        df2['O3 Mean'] = df2['O3 Mean'].map(lambda x: float(x))
        df3['O3 Mean'] = df3['O3 Mean'].map(lambda x: float(x))

        df1['O3 AQI'] = df1['O3 AQI'].map(lambda x: float(x))
        df2['O3 AQI'] = df2['O3 AQI'].map(lambda x: float(x))
        df3['O3 AQI'] = df3['O3 AQI'].map(lambda x: float(x))

        df1['O3 1st Max Hour'] = df1['O3 1st Max Hour'].map(lambda x: float(x))
        df2['O3 1st Max Hour'] = df2['O3 1st Max Hour'].map(lambda x: float(x))
        df3['O3 1st Max Hour'] = df3['O3 1st Max Hour'].map(lambda x: float(x))

        df1['year'] = df1['Date Local'].map(lambda x: int(x[0:x.index('/')]))
        df1['month'] = df1['Date Local'].map(lambda x: int(x[5:x.rindex('/')]))
        df2['year'] = df2['Date Local'].map(lambda x: int(x[0:x.index('/')]))
        df2['month'] = df2['Date Local'].map(lambda x: int(x[5:x.rindex('/')]))
        df3['year'] = df3['Date Local'].map(lambda x: int(x[0:x.index('/')]))
        df3['month'] = df3['Date Local'].map(lambda x: int(x[5:x.rindex('/')]))
        
        df_mean1 = df1.loc[:, ['O3 Mean', 'year', 'month']]
        df_mean2 = df2.loc[:, ['O3 Mean', 'year', 'month']]
        df_mean3 = df3.loc[:, ['O3 Mean', 'year', 'month']]
        df_mean1_groupby = df_mean1.groupby(['year', 'month'], as_index=False).mean()
        df_mean2_groupby = df_mean2.groupby(['year', 'month'], as_index=False).mean()
        df_mean3_groupby = df_mean3.groupby(['year', 'month'], as_index=False).mean()
        df11 = df_mean1_groupby.sort_values(['year', 'month'])  # 按照月份从小到大排序
        df22 = df_mean2_groupby.sort_values(['year', 'month'])  # 按照月份从小到大排序
        df22 = df22.dropna()
        df33 = df_mean3_groupby.sort_values(['year', 'month'])  # 按照月份从小到大排序
        df11['year-month']=df11['year'].map(lambda x: str(x))+'-'+df11['month'].map(lambda x: str(x))
        df22['year-month']=df22['year'].map(lambda x: str(x))+'-'+df22['month'].map(lambda x: str(x))
        df33['year-month']=df33['year'].map(lambda x: str(x))+'-'+df33['month'].map(lambda x: str(x))

        df_mean4 = df1.loc[:, ['O3 AQI', 'year', 'month']]
        df_mean5 = df2.loc[:, ['O3 AQI', 'year', 'month']]
        df_mean6 = df3.loc[:, ['O3 AQI', 'year', 'month']]
        df_mean4_groupby = df_mean4.groupby(['year', 'month'], as_index=False).mean()
        df_mean5_groupby = df_mean5.groupby(['year', 'month'], as_index=False).mean()
        df_mean6_groupby = df_mean6.groupby(['year', 'month'], as_index=False).mean()
        df111 = df_mean4_groupby.sort_values(['year', 'month'])  # 按照月份从小到大排序
        df222 = df_mean5_groupby.sort_values(['year', 'month'])  # 按照月份从小到大排序
        df333 = df_mean6_groupby.sort_values(['year', 'month'])  # 按照月份从小到大排序
        df111['year-month']=df111['year'].map(lambda x: str(x))+'-'+df111['month'].map(lambda x: str(x))
        df222['year-month']=df222['year'].map(lambda x: str(x))+'-'+df222['month'].map(lambda x: str(x))
        df333['year-month']=df333['year'].map(lambda x: str(x))+'-'+df333['month'].map(lambda x: str(x))

        df_mean7 = df1.loc[:, ['O3 1st Max Hour', 'year', 'month']]
        df_mean8 = df2.loc[:, ['O3 1st Max Hour', 'year', 'month']]
        df_mean9 = df3.loc[:, ['O3 1st Max Hour', 'year', 'month']]
        df_mean7_groupby = df_mean7.groupby(['year', 'month'], as_index=False).mean()
        df_mean8_groupby = df_mean8.groupby(['year', 'month'], as_index=False).mean()
        df_mean9_groupby = df_mean9.groupby(['year', 'month'], as_index=False).mean()
        df1111 = df_mean7_groupby.sort_values(['year', 'month'])  # 按照月份从小到大排序
        df2222 = df_mean8_groupby.sort_values(['year', 'month'])  # 按照月份从小到大排序
        df2222 = df2222.dropna()
        df3333 = df_mean9_groupby.sort_values(['year', 'month'])  # 按照月份从小到大排序
        df1111['year-month']=df1111['year'].map(lambda x: str(x))+'-'+df1111['month'].map(lambda x: str(x))
        df2222['year-month']=df2222['year'].map(lambda x: str(x))+'-'+df2222['month'].map(lambda x: str(x))
        df3333['year-month']=df3333['year'].map(lambda x: str(x))+'-'+df3333['month'].map(lambda x: str(x))
        
        try:

            plt.figure(figsize=(12, 8))  # 作图的大小
            plt.plot(range(len(list(df11['year-month']))), df11['O3 Mean'], label='Houston', color='red', marker='o')
            plt.xticks(range(len(list(df11['year-month']))), list(df11['year-month']), rotation=90)
            plt.plot(range(len(list(df22['year-month']))), df22['O3 Mean'], label='New York', color='green', marker='o')
            plt.xticks(range(len(list(df22['year-month']))), list(df22['year-month']),rotation=90)
            plt.plot(range(len(list(df33['year-month']))), df33['O3 Mean'], label='Washington', color='blue', marker='o')
            plt.xticks(range(len(list(df33['year-month']))), list(df33['year-month']), rotation=90)
            plt.title('Houston_NewYork_Washington_2007_2009_O3Mean', fontproperties='SimHei', fontsize=14)
            plt.xlabel('X-年月', fontproperties='SimHei', fontsize=14)
            plt.ylabel('Y-O3 Mean值', fontproperties='SimHei', fontsize=14)
            plt.legend()
            plt.savefig('Houston_NewYork_Washington_2007_2009_O3Mean.png', dpi=300)
            plt.show()

            plt.figure(figsize=(12, 8))  # 作图的大小
            plt.plot(range(len(list(df111['year-month']))), df111['O3 AQI'], label='Houston', color='red', marker='o')
            plt.xticks(range(len(list(df111['year-month']))), list(df111['year-month']), rotation=90)
            plt.plot(range(len(list(df222['year-month']))), df222['O3 AQI'], label='New York', color='green', marker='o')
            plt.xticks(range(len(list(df222['year-month']))), list(df222['year-month']),rotation=90)
            plt.plot(range(len(list(df333['year-month']))), df333['O3 AQI'], label='Washington', color='blue', marker='o')
            plt.xticks(range(len(list(df333['year-month']))), list(df333['year-month']), rotation=90)
            plt.title('Houston_NewYork_Washington_2007_2009_O3AQI', fontproperties='SimHei', fontsize=14)
            plt.xlabel('X-年月', fontproperties='SimHei', fontsize=14)
            plt.ylabel('Y-O3 AQI值', fontproperties='SimHei', fontsize=14)
            plt.legend()
            plt.savefig('Houston_NewYork_Washington_2007_2009_O3AQI.png', dpi=300)
            plt.show()

            plt.figure(figsize=(12, 8))  # 作图的大小
            plt.plot(range(len(list(df1111['year-month']))), df1111['O3 1st Max Hour'], label='Houston', color='red', marker='o')
            plt.xticks(range(len(list(df1111['year-month']))), list(df1111['year-month']), rotation=90)
            plt.plot(range(len(list(df2222['year-month']))), df2222['O3 1st Max Hour'], label='New York', color='green', marker='o')
            plt.xticks(range(len(list(df2222['year-month']))), list(df2222['year-month']),rotation=90)
            plt.plot(range(len(list(df3333['year-month']))), df3333['O3 1st Max Hour'], label='Washington', color='blue', marker='o')
            plt.xticks(range(len(list(df3333['year-month']))), list(df3333['year-month']), rotation=90)
            plt.title('Houston_NewYork_Washington_2007_2009_O3_1st_Max_Hour', fontproperties='SimHei', fontsize=14)
            plt.xlabel('X-年月', fontproperties='SimHei', fontsize=14)
            plt.ylabel('Y-O3 1st Max Hour值', fontproperties='SimHei', fontsize=14)
            plt.legend()
            plt.savefig('Houston_NewYork_Washington_2007_2009_O3_1st_Max_Hour.png', dpi=300)
            plt.show()
            print('任务5执行成功！')
        except:
            print("任务5执行不成功！")
    except:
        print('任务5执行不成功！')


# 系统主界面
def menu():
    print('[任务选择]\n'
          '+-----美国五个著名城市空气质量分析及可视化系统----+\n'
          '|0、退出。                                    |\n'
          '|1、数据读取。                          |\n'
          '|2、数据预处理及导出。                            |\n'
          '|3、数据选择及导出。                            |\n'
          '|4、数据选择与转存。                             |\n'
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
            if os.path.exists('3.pollution_us_5city_2006_2010_O3.csv'):
                dataconduction()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '3':
            if os.path.exists('pollution_us_5city_2007_2009_O3.csv'):
                dataselection()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '4':
            if os.path.exists('pollution_us_Houston_2007_2009_O3.txt' and 'pollution_us_NewYork_2007_2009_O3.txt' and 'pollution_us_Washington_2007_2009_O3.txt'):
                datainventory()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '5':
            if os.path.exists('pollution_us_Houston_2007_2009_O3.xlsx'):
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