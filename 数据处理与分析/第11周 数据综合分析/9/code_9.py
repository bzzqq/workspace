##############################################################
# 系统主界面
def menu():
    print('[任务选择]\n'
          '+------2008—2013年世界各国PM2.5数据分析及可视化系统------+\n'
          '|0、退出。                                             |\n'
          '|1、数据读取。                                   |\n'
          '|2、数据处理并选择及导出。                                     |\n' 
          '|3、数据统计计算。                                      |\n'
          '|4、数据可视化。                                        |\n'
          '+------------------------------------------------------+')



import pandas as pd
import matplotlib.pyplot as plt
import os

# 防止中文出现乱码
plt.rcParams['font.sans-serif'] = ['SimHei']   # 黑体
plt.rcParams['axes.unicode_minus'] = False

#任务【1】
def datapreprocessing():  # 加工数据
        filename = input('请输入要打开的文件名9.world_pm25_pm10.csv:')  # 读取数据
        try:
            df = pd.read_csv(filename, encoding='cp936')  # 读文件
            df = df.dropna()  # 丢弃缺失值
            df.to_csv('world_pm25_pm10P.csv', encoding='cp936', index=False)   # 导出新文件
            print(df.head(5))  # 查看前五行
            print(df.tail(2))  # 查看后两行
            print('任务1执行成功！')
        except:  # 处理异常语句
            print('任务1执行不成功！')
#任务【2】
def dataselection():
        filename = input("请输入要打开的文件名world_pm25_pm10P.csv：")
        try:
            df = pd.read_csv(filename, encoding='cp936')
            df_new = df.loc[:,['Region', 'Country', 'City/station', 'PM 2.5', 'PM2.5 Year']]
            try:
                df_new.to_csv('world_pm25.txt', encoding='cp936', index=False,sep=' ')#错误：未按空格间隔
                print("任务2执行成功！")
            except:
                print("任务2执行不成功")
        except:
            print("任务2执行不成功")
#任务【3】
def datadescribe():
        filename = input('请输入要打开的文件名world_pm25.txt:')
        try:
            df_new1 = pd.read_csv(filename, encoding='cp936',sep=' ')
            df_new1['PM 2.5'] = df_new1['PM 2.5'].map(lambda x: float(x))
            df_new = df_new1.sort_values('PM 2.5', ascending=False)
            df_new.to_csv('world_pm25_descending.csv', index=False)
            print("任务3执行成功！")
        except:
            print("任务3执行不成功！")
#任务【4】
def datavisualization():
        filename = input("请输入要打开的文件名world_pm25_descending.csv:")
        try:
            df_new2 = pd.read_csv(filename, encoding='cp936')
            data = df_new2['PM 2.5']
            category = [0, 50, 100, 150, 200]
            labels = ['One', 'Two', 'Three', 'Four']
            data_cut = pd.cut(data, category, right=False, labels=labels)
            print(data_cut)
            data_cut_counts = data_cut.value_counts()
            print(data_cut_counts)
            plt.figure()
            data_cut_counts.plot(kind='bar', figsize=(12, 8))
            plt.title('PM 2.5离散化统计柱状图', fontproperties='SimHei', fontsize=14)  # 标题、字体、大小
            plt.savefig('world_pm25_hist.png', dpi=300)  # 保存图表，分辨率为300dpi
            plt.show()  # 展示图表
            data_cut_counts.plot(kind='pie', figsize=(12, 8))
            plt.title('PM 2.5离散化统计饼状图', fontproperties='SimHei', fontsize=14)  # 标题、字体、大小
            plt.savefig('world_pm25_pie.png', dpi=300)  # 保存图表，分辨率为300dpi
            plt.show()  # 展示图表
            print('任务4执行成功！')
        except:
            print('任务4执行不成功！')



###############################################################
# 功能选择模块
def task():
    while True:
        menu()  # 打印系统主界面
        num = input("请输入任务选项：")
        if num == '1':
            datapreprocessing()
        elif num == '2':
            if os.path.exists('world_pm25_pm10P.csv'):
                dataselection()
            else:
                print("未能实行当前选项，请先执行前面的选项！")
        elif num == '3':
            if os.path.exists('world_pm25.txt'):
                datadescribe()
            else:
                print("未能实行当前选项，请先执行前面的选项！")
        elif num == '4':
            if os.path.exists('world_pm25_descending.csv'):
                datavisualization()
            else:
                print("未能实行当前选项，请先执行前面的选项！")
        elif num == '0':
            print("程序结束!")
            break
        else:
            print("输入选项有误")
        input("回车显示菜单")
################################################################

####################################
# 主函数
if __name__ == '__main__':
    task()  # 调用功能选择函数