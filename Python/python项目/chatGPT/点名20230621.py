import tkinter as tk
import random


class RollCallApp:
    def __init__(self, students):
        self.students = students
        self.current_student = ""
        self.roll_call_running = False
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="")
        self.button = tk.Button(self.root, text="开始点名", command=self.toggle_roll_call)
        self.label.pack()
        self.button.pack()

    def toggle_roll_call(self):
        if self.roll_call_running:
            self.stop_roll_call()
        else:
            self.start_roll_call()

    def start_roll_call(self):
        if not self.roll_call_running:
            self.roll_call_running = True
            self.roll_call()

    def stop_roll_call(self):
        self.roll_call_running = False

    def roll_call(self):
        if self.roll_call_running:
            self.current_student = random.choice(self.students)
            self.label.config(text=self.current_student)
            self.label.after(200, self.roll_call)
        else:
            self.label.config(text=self.current_student)

    def run(self):
        self.root.mainloop()


# 学生名单
students = ["学生1", "学生2", "学生3", "学生4", "学生5", "学生6", "学生7", "学生8", "学生9", "学生10"]

app = RollCallApp(students)
app.run()
