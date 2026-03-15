import random
import tkinter as tk


class RollCallApp:
    def __init__(self, students):
        self.students = students
        self.roll_call_running = False

        self.window = tk.Tk()
        self.window.title("班级点名程序")
        self.window.geometry("400x200")

        self.student_name = tk.StringVar()
        self.student_name.set("请开始点名")

        self.label = tk.Label(self.window, textvariable=self.student_name, font=("微软雅黑", 24), fg="red")
        self.label.pack(pady=20)

        self.button = tk.Button(self.window, text="开始点名", font=("微软雅黑", 16),  command=self.roll_call)
        self.button.pack(pady=10)

    def roll_call(self):
        if not self.roll_call_running:
            self.roll_call_running = True
            self.button.config(text="停止滚动")
            self.roll_call_loop()
        else:
            self.roll_call_running = False
            self.button.config(text="开始点名")

    def roll_call_loop(self):
        student = random.choice(self.students)
        self.student_name.set(student)

        if self.roll_call_running:
            self.window.after(100, self.roll_call_loop)

    def run(self):
        self.window.mainloop()


students = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Harry", "Isabella", "Jack", "Kevin", "Lily", "Maggie", "Nancy", "Oliver", "Peter"]


students2 = ["张三", "赵四", "王五", "李六"]

app = RollCallApp(students2)
app.run()
