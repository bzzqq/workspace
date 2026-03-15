import pandas as pd
import matplotlib.pyplot as plt
import os

# 防止中文出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False


# 任务【1】
def datapreprocessing():
        filename = input('请输入要打开的文件名8.PRSA_data_2010.1.1-2014.12.31.csv:')  # 打开文件
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读取数据
            print(df.head(3))  # 查看前三行内容
            print(df.tail(2))  # 查看后两行内容
            df = df.dropna()
            print('任务1执行成功！')
        except:  # 任务执行不成功时输出的代码
            print('任务1执行不成功，请重新输入！')


# 任务【2】
def dataconduction():
        filename = input('请输入要打开的文件名8.PRSA_data_2010.1.1-2014.12.31.csv：')  # 打开文件
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读取数据
            df.drop(columns=['pm2.5', 'DEWP', 'TEMP', 'PRES', 'Is', 'Ir'], axis=1, inplace=True)
            df.to_csv('8.Iws_data_2010.1.1-2014.12.31.csv', encoding='cp936', index=False)
            print("任务2执行成功！")
        except:
            print("任务2执行不成功，请重新输入！")


# 任务【3】
def dataselection():
        filename = input('请输入要打开的文件名8.Iws_data_2010.1.1-2014.12.31.csv：')
        try:
            df = pd.read_csv(filename, encoding='cp936')
            df_new1 = df[df['cbwd'] == 'NW']
            df_new2 = df[df['cbwd'] == 'NE']
            df_new3 = df[df['cbwd'] == 'SE']
            df_new4 = df[df['cbwd'] == 'cv']
            try:
                df_new1.to_csv('8.Iws_NW_data_2010.1.1-2014.12.31.txt', encoding='cp936', index=False)
                df_new2.to_csv('8.Iws_NE_data_2010.1.1-2014.12.31.txt', encoding='cp936', index=False)
                df_new3.to_csv('8.Iws_SE_data_2010.1.1-2014.12.31.txt', encoding='cp936', index=False)
                df_new4.to_csv('8.Iws_cv_data_2010.1.1-2014.12.31.txt', encoding='cp936', index=False)
                print("任务3执行成功！")
            except:
                print("任务3执行失败！")
        except:
            print("任务3执行失败！")


# 任务【4】
def datainventory():
    filename1 = input('请输入要打开的文件名8.Iws_NW_data_2010.1.1-2014.12.31.txt：')
    filename2 = input('请输入要打开的文件名8.Iws_NE_data_2010.1.1-2014.12.31.txt：')
    filename3 = input('请输入要打开的文件名8.Iws_SE_data_2010.1.1-2014.12.31.txt：')
    filename4 = input('请输入要打开的文件名8.Iws_cv_data_2010.1.1-2014.12.31.txt：')
    try:
        df1 = pd.read_csv(filename1, encoding='cp936')
        df1.to_excel('8.Iws_NW_data_2010.1.1-2014.12.31.xlsx', encoding='cp936', index=False)
        df2 = pd.read_csv(filename2, encoding='cp936')
        df2.to_excel('8.Iws_NE_data_2010.1.1-2014.12.31.xlsx', encoding='cp936', index=False)
        df3 = pd.read_csv(filename3, encoding='cp936')
        df3.to_excel('8.Iws_SE_data_2010.1.1-2014.12.31.xlsx', encoding='cp936', index=False)
        df4 = pd.read_csv(filename4, encoding='cp936')
        df4.to_excel('8.Iws_cv_data_2010.1.1-2014.12.31.xlsx', encoding='cp936', index=False)
        print("任务4执行成功！")
    except:
        print("任务4执行失败，请重试！")


# 任务【5】
def datavisualization():
    filename1 = input('请输入要打开的文件名8.Iws_NW_data_2010.1.1-2014.12.31.xlsx：')
    filename2 = input('请输入要打开的文件名8.Iws_NE_data_2010.1.1-2014.12.31.xlsx：')
    filename3 = input('请输入要打开的文件名8.Iws_SE_data_2010.1.1-2014.12.31.xlsx：')
    filename4 = input('请输入要打开的文件名8.Iws_cv_data_2010.1.1-2014.12.31.xlsx：')
    try:
        df1 = pd.read_excel(filename1, encoding='cp936')
        df_new1 = df1[df1['Iws'] >8]
        df_mean = df_new1.loc[:, ['year', 'Iws']]
        df_mean_groupby = df_mean.groupby(['year'], as_index=False).mean()
        df11 = df_mean_groupby.sort_values(['year'])  # 按照月份从小到大排序
        plt.figure(figsize=(12, 8))  # 作图的大小
        y1 = df11['Iws']
        names1 = ['2010', '2011', '2012', '2013', '2014']
        plt.plot(range(5), y1, color='red')
        plt.xticks(range(5), names1)
        plt.title('Iws_NW_data年均值', fontproperties='SimHei', fontsize=14)
        plt.xlabel('X-年份', fontproperties='SimHei', fontsize=14)
        plt.ylabel('Y-Iws_NW_data年平均值', fontproperties='SimHei', fontsize=14)
        plt.savefig('Iws_NW_data_Mean.png', dpi=300)
        plt.show()

        df2 = pd.read_excel(filename2, encoding='cp936')
        df_new2 = df2[df2['Iws'] >8]
        df_mean2 = df_new2.loc[:, ['year', 'Iws']]
        df_mean2_groupby = df_mean2.groupby(['year'], as_index=False).mean()
        df22 = df_mean2_groupby.sort_values(['year'])  # 按照月份从小到大排序
        plt.figure(figsize=(12, 8))  # 作图的大小
        y2 = df22['Iws']
        names2 = ['2010', '2011', '2012', '2013', '2014']
        plt.plot(range(5), y2, color='green')
        plt.xticks(range(5), names2)
        plt.title('Iws_NE_data年均值', fontproperties='SimHei', fontsize=14)
        plt.xlabel('X-年份', fontproperties='SimHei', fontsize=14)
        plt.ylabel('Y-Iws_NE_data年平均值', fontproperties='SimHei', fontsize=14)
        plt.savefig('Iws_NE_data_Mean.png', dpi=300)
        plt.show()

        df3 = pd.read_excel(filename3, encoding='cp936')
        df_new3 = df3[df3['Iws'] >8]
        df_mean3 = df_new3.loc[:, ['year', 'Iws']]
        df_mean3_groupby = df_mean3.groupby(['year'], as_index=False).mean()
        df33 = df_mean3_groupby.sort_values(['year'])  # 按照月份从小到大排序
        plt.figure(figsize=(12, 8))  # 作图的大小
        y3 = df33['Iws']
        names3 = ['2010', '2011', '2012', '2013', '2014']
        plt.plot(range(5), y3, color='blue')
        plt.xticks(range(5), names3)
        plt.title('Iws_SE_data年均值', fontproperties='SimHei', fontsize=14)
        plt.xlabel('X-年份', fontproperties='SimHei', fontsize=14)
        plt.ylabel('Y-Iws_SE_data年平均值', fontproperties='SimHei', fontsize=14)
        plt.savefig('Iws_SE_data_Mean.png', dpi=300)
        plt.show()

        df4 = pd.read_excel(filename4, encoding='cp936')
        df_new4 = df4[df4['Iws'] >8]
        df_mean4 = df_new4.loc[:, ['year', 'Iws']]
        df_mean4_groupby = df_mean4.groupby(['year'], as_index=False).mean()
        df44 = df_mean4_groupby.sort_values(['year'])  # 按照月份从小到大排序
        plt.figure(figsize=(12, 8))  # 作图的大小
        y4 = df44['Iws']
        names4 = ['2010', '2011', '2012', '2013', '2014']
        plt.plot(range(5), y4, color='black')
        plt.xticks(range(5), names4)
        plt.title('Iws_cv_data年均值', fontproperties='SimHei', fontsize=14)
        plt.xlabel('X-年份', fontproperties='SimHei', fontsize=14)
        plt.ylabel('Y-Iws_cv_data年平均值', fontproperties='SimHei', fontsize=14)
        plt.savefig('Iws_cv_data_Mean.png', dpi=300)
        plt.show()



        print("任务5执行成功！")
    except:
        print("任务5执行失败，请重试！")

# 系统主界面
def menu():
    print('[任务选择]\n'
          '+-----2010-2014年北京市风力数据分析及可视化系统----+\n'
          '|0、退出。                                      |\n'
          '|1、数据读取。                            |\n'
          '|2、数据预处理及导出。                              |\n'
          '|3、数据选择及导出。                              |\n'
          '|4、数据转存。                                   |\n'
          '|5、数据可视化。                                 |\n'
          '+-----------------------------------------------+')


# 功能选择模块
def task():
    while True:
        menu()  # 打印系统主界面
        num = input("请输入任务选项：")
        if num == '1':
            datapreprocessing()
        elif num == '2':
            if os.path.exists('8.PRSA_data_2010.1.1-2014.12.31.csv'):
                dataconduction()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '3':
            if os.path.exists('8.Iws_data_2010.1.1-2014.12.31.csv'):
                dataselection()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '4':
            if os.path.exists('8.Iws_NW_data_2010.1.1-2014.12.31.txt'
                              and '8.Iws_NE_data_2010.1.1-2014.12.31.txt'
                              and '8.Iws_SE_data_2010.1.1-2014.12.31.txt'
                              and '8.Iws_cv_data_2010.1.1-2014.12.31.txt'):
                datainventory()
            else:
                print('未能执行当前选项，请先执行前面的选项')
        elif num == '5':
            if os.path.exists('8.Iws_NW_data_2010.1.1-2014.12.31.xlsx'
                              and '8.Iws_NE_data_2010.1.1-2014.12.31.xlsx'
                              and '8.Iws_SE_data_2010.1.1-2014.12.31.xlsx'
                              and '8.Iws_cv_data_2010.1.1-2014.12.31.xlsx'):
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