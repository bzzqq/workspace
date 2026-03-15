import random  # 导入随机模块
import pyttsx3  # 导入第三方语音模块
import tkinter as tk  # 导入Tkinter模块
from tkinter import filedialog  # 导入filedialog模块

listen = pyttsx3.init()  # 初始化
window = tk.Tk()  # 创建窗口对象
window.title('随机点名')  # 设置窗口标题
window.geometry('300x200')  # 设置窗口大小


def select_file():  # 定义事件处理函数
    global txt_path  # 声明全局变量
    txt_path = filedialog.askopenfilename(title='请选择txt文件',
                                          filetypes=[('TXT', '*.txt')
                                                     ])  # 弹出文件选择对话框，并获取选中的文件路径


button1 = tk.Button(window, text='选择txt文件',
                    command=select_file)  # 创建按钮组件，并绑定事件处理函数
button1.pack()  # 布局按钮组件


def call_name():  # 定义事件处理函数
    with open(txt_path, encoding='utf-8') as f:  # 打开文件
        names = f.readlines()  # 读取所有行
        name = random.choice(names)  # 随机选择一个姓名
        listen.say(name)  # 说出姓名
        listen.runAndWait()  # 开始输出语音


button2 = tk.Button(window, text='开始点名', command=call_name)  # 创建按钮组件，并绑定事件处理函数
button2.pack()  # 布局按钮组件

window.mainloop()  # 启动主循环
