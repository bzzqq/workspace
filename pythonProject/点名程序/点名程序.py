import tkinter as tk

# 定义学生名单
class_students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
class2_students = ['Frank', 'Grace', 'Hannah', 'Isaac', 'Jack']

# 初始化当前班级和学生列表
current_class = class_students
current_student = 0
is_rolling = False


def toggle_roll():
    """开始/停止名字循环滚动"""
    global is_rolling
    if is_rolling:
        is_rolling = False
        roll_button.config(text="开始")
    else:
        is_rolling = True
        roll_button.config(text="停止")
        start_rolling()


def start_rolling():
    """开始名字循环滚动"""
    global current_class, current_student
    if is_rolling:
        selected_student = current_class[current_student]
        result_label.config(text=selected_student)
        current_student = (current_student + 1) % len(current_class)
        window.after(1000, start_rolling)  # 每隔0.1秒滚动名字


def select_class(event):
    """选择班级时的回调函数"""
    selected_class = class_var.get()
    global current_class, current_student
    if selected_class == "班级1":
        current_class = class_students
    elif selected_class == "班级2":
        current_class = class2_students
    current_student = 0


# 创建主窗口
window = tk.Tk()
window.title("点名程序")
window.geometry("1400x400")

# 创建班级选择下拉菜单
class_var = tk.StringVar()
class_var.set("班级1")  # 默认选择班级1
class_dropdown = tk.OptionMenu(window, class_var, "班级1", "班级2")
class_dropdown.config(font=("微软雅黑", 50))  # 设置菜单的字体大小
class_var.trace_add("write", select_class)  # 绑定选择班级的回调函数

# 创建标签用于显示结果
result_label = tk.Label(window, text="点击按钮开始点名", font=("微软雅黑", 120))
result_label.pack()

# 使用place布局管理器将组件定位到指定位置
class_dropdown.place(x=300, y=250)

# 创建开始/停止按钮，并将按钮固定在指定位置
roll_button = tk.Button(window, text="开始", font=("微软雅黑", 50), command=toggle_roll)
roll_button.place(x=700, y=250)

# 运行主循环
window.mainloop()
