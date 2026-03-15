import random  # 导入随机模块
import pyttsx3  # 导入第三方语音模块
import tkinter as tk  # 导入Tkinter模块

listen = pyttsx3.init()  # 初始化
window = tk.Tk()  # 创建窗口对象
window.title('随机点名')  # 设置窗口标题
window.geometry('800x600')  # 设置窗口大小

# label = tk.Label(window, text='请输入txt文件的path:')  # 创建标签组件
# label.pack()  # 布局标签组件

# entry = tk.Entry(window)  # 创建输入框组件
# entry.pack()  # 布局输入框组件


def call_name():  # 定义事件处理函数
    txt_path = "D:/新建文本文档.txt"  # 获取输入框内容
    with open(txt_path, encoding='utf-8') as f:  # 打开文件
        names = f.readlines()  # 读取所有行
        name = random.choice(names)  # 随机选择一个姓名
        print(name)
        listen.say(name)  # 说出姓名
        listen.runAndWait()  # 开始输出语音


button = tk.Button(window, text='开始点名', command=call_name)  # 创建按钮组件，并绑定事件处理函数
button.pack()  # 布局按钮组件

window.mainloop()  # 启动主循环
