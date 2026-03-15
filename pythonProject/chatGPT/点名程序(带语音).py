import random  # 导入随机模块
import pyttsx3  # 导入第三方语音模块

listen = pyttsx3.init()  # 初始化
# txt_path = input('请输入txt文件的path:')   输入名单文件的路径
txt_path = "D:/新建文本文档.txt"
# D:\新建文本文档.txt
with open(txt_path, encoding='utf-8') as f:  # 打开文件
    names = f.readlines()  # 读取所有行
    name = random.choice(names)  # 随机选择一个姓名
    print(name)
    listen.say(name)  # 说出姓名
    listen.runAndWait()  # 开始输出语音
