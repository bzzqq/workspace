# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import os
#防止出现乱码
plt.rcParams['font.sans-serif']=['SimHei']#黑体
plt.rcParams['axes.unicode_minus'] = False
#【任务1】
def dataPreprocessing():
        #读取数据
        fileName=input('请输入要打开的文件名24.presidential_polls.csv:')
        try:
            df=pd.read_csv(fileName,encoding='cp936')
            #查看前5行
            print(df.head(5))
            #查看后2行
            print(df.tail(2))            
            print('任务1执行成功')
        except:
            print('任务1执行失败')
#【任务2】
def dataSelection():
        #读取数据
        fileName=input('请输入要打开的文件名24.presidential_polls.csv:')
        try:
            df=pd.read_csv(fileName,encoding='cp936')
            df.dropna()#丢弃缺失值
            df_new=df.loc[:,['state','rawpoll_clinton','adjpoll_clinton']]
            df_new.to_csv('presidential_polls_clinton.txt',sep=' ',index=False)
            print('任务2执行成功')
        except:
            print('任务2执行失败')
#【任务3】
def dataGroup():
        #读取数据
        fileName=input('请输入要打开的文件名presidential_polls_clinton.txt:')
        try:
            df_new=pd.read_csv(fileName,encoding='cp936',sep=' ')
            df_new_group=df_new.groupby(['state'],as_index=False).mean()
            df_new_group.to_excel('presidential_polls_clinton_state_mean.xlsx',encoding='cp936',index=False)
            print('任务3执行成功')
        except:
            print('任务3执行失败')
#【任务4】
def dataCalculate():
        #读取数据
        fileName=input('请输入要打开的文件presidential_polls_clinton_state_mean.xlsx:')
        try:
            df_mean=pd.read_excel(fileName,encoding='cp936')
            category=[0,25,50,75,100]
            labels=['OneSup','TwoSup','ThreeSup','FourSup']
            df_mean['Label']=pd.cut(df_mean['adjpoll_clinton'],category,right=False,labels=labels)
            df_mean.to_csv('presidential_polls_clinton_state_mean_lable.csv',encoding='cp936',sep=' ',index=False)#错误：未以空格间隔，错误的保存了行索引
            print('任务4执行成功')
        except:
            print('任务4执行失败')
#【任务5】
def dataVisualization():
        #读取数据
        fileName=input('请输入要打开的文件名presidential_polls_clinton_state_mean_lable.csv:')
        try:
            df_Label=pd.read_csv(fileName,encoding='cp936',sep=' ')
            df_cLabel=df_Label['Label'].value_counts()
            x=['OneSup','TwoSup','ThreeSup','FourSup']
            y=[df_cLabel.get('OneSup',0),df_cLabel.get('TwoSup',0),df_cLabel.get('ThreeSup',0),df_cLabel.get('FourSup',0)]
            plt.figure()
            plt.bar(range(len(x)),y,color='blue',label='Numerical value')
            plt.xticks(range(len(x)), x)
            plt.title('presidential_polls_clinton_state_support')
            plt.xlabel('Numerical value')
            plt.ylabel('Interval')
            plt.legend()
            plt.savefig('presidential_polls_clinton_state_support.png',dpi=400)
            plt.show()
            print('任务5执行成功')
        except:
            print('任务5执行失败')
#系统主界面
def menu():
    print('[任务选择]\n'
           '+——————presidential_polls_visualization————————+\n'
           '|0、退出                                    |\n'
           '|1、数据读取                         |\n'
           '|2、数据预处理及切片                                |\n'
           '|3、数据分类                                |\n'
           '|4、数据统计                                |\n'
           '|5、数据可视化                              |\n'
           '+—————————————————————————————————————————————+')
#功能选择模块
def task():
    while True:
        menu()    #打印主界面
        num=input('请输入任务选项:')
        if num=='1':
            dataPreprocessing()
        elif num == '2':
            if os.path.exists('24.presidential_polls.csv'):
                dataSelection()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '3':
            if os.path.exists('presidential_polls_clinton.txt'):
                dataGroup()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '4':
            if os.path.exists('presidential_polls_clinton_state_mean.xlsx'):
                dataCalculate()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '5':
            if os.path.exists('presidential_polls_clinton_state_mean_lable.csv'):
                dataVisualization()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num =='0':
            print('程序结束')
            break
        else:
            print('输入选项有误')
        input('回车显示菜单')
#主函数
if __name__ == '__main__' :
    task()     #调用功能选择函数
            
