import tkinter as tk
import random
import time


class StudentPicker:
    def __init__(self, master, students):
        self.master = master
        self.students = students
        self.current_student = None
        self.running = False

        self.label = tk.Label(master, text="请按'开始'键", font=("微软雅黑", 18), foreground="red")
        self.label.pack(pady=50)

        self.start_button = tk.Button(master, text="开始", font=("微软雅黑", 16), command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = tk.Button(master, text="停止", font=("微软雅黑", 16), command=self.stop, state=tk.DISABLED)
        self.stop_button.pack(side=tk.RIGHT, padx=20)

    def start(self):
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        while self.running:
            student = random.choice(self.students)
            while student == self.current_student:
                student = random.choice(self.students)
            self.current_student = student
            self.label.config(text=self.current_student)
            self.master.update()
            time.sleep(0.1)

    def stop(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.label.config(text=random.choice(self.students))


students = [
    "Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Harry",
    "Isabella", "Jack", "Kevin", "Lily", "Maggie", "Nancy", "Oliver", "Peter",
    "Queen", "Robert", "Sarah", "Tom", "Uma", "Victor", "Wendy", "Xander",
    "Yvonne", "Zoe", "Alan", "Ben", "Cathy", "Daniel"
]


students2 = [
    "张三", "李四", "王五"
]

root = tk.Tk()
root.title("Student Picker")
root.geometry("400x200")
app = StudentPicker(root, students2)
root.mainloop()
