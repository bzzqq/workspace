import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import random

class RollCallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("课堂点名程序 - Python数据处理与分析")
        self.root.geometry("1000x700")
        
        # 加载数据
        self.load_data()
        
        # 点名记录
        self.called_students = []
        self.remaining_students = []
        self.current_student = None
        self.is_rolling = False
        
        self.setup_ui()
        self.reset_remaining()
        
    def load_data(self):
        """从Excel文件加载学生数据"""
        try:
            # 读取Excel文件，第一行是表头
            df = pd.read_excel('点名册.xlsx')
            # 选择需要的列
            self.students = df[['序号', '学号', '姓名', '班级']].to_dict('records')
            self.total_students = len(self.students)
            print(f"成功加载 {self.total_students} 名学生")
        except Exception as e:
            messagebox.showerror("错误", f"无法加载学生数据：{str(e)}")
            self.students = []
            self.total_students = 0
    
    def reset_remaining(self):
        """重置剩余学生列表"""
        self.remaining_students = self.students.copy()
        random.shuffle(self.remaining_students)
    
    def setup_ui(self):
        """设置用户界面"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 标题
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill=tk.X, pady=(0, 15))
        
        title_label = ttk.Label(title_frame, text="📚 课堂随机点名程序", 
                               font=('微软雅黑', 24, 'bold'))
        title_label.pack()
        
        # 课程信息
        course_label = ttk.Label(title_frame, 
                               text="《Python数据处理与分析》 | 1-12周 周二3-4节 | 渤海渤1教-3314",
                               font=('微软雅黑', 11))
        course_label.pack(pady=(5, 0))
        
        # 统计信息卡片
        stats_frame = ttk.Frame(main_frame)
        stats_frame.pack(fill=tk.X, pady=10)
        
        # 总人数卡片
        total_card = ttk.Frame(stats_frame, relief='solid', borderwidth=1)
        total_card.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.BOTH)
        ttk.Label(total_card, text="总人数", font=('微软雅黑', 10)).pack(pady=(5, 0))
        self.total_label = ttk.Label(total_card, text=str(self.total_students), 
                                   font=('微软雅黑', 20, 'bold'))
        self.total_label.pack(pady=(0, 5))
        
        # 已点名卡片
        called_card = ttk.Frame(stats_frame, relief='solid', borderwidth=1)
        called_card.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.BOTH)
        ttk.Label(called_card, text="已点名", font=('微软雅黑', 10)).pack(pady=(5, 0))
        self.called_label = ttk.Label(called_card, text="0", 
                                    font=('微软雅黑', 20, 'bold'), foreground='green')
        self.called_label.pack(pady=(0, 5))
        
        # 剩余人数卡片
        remaining_card = ttk.Frame(stats_frame, relief='solid', borderwidth=1)
        remaining_card.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.BOTH)
        ttk.Label(remaining_card, text="剩余", font=('微软雅黑', 10)).pack(pady=(5, 0))
        self.remaining_label = ttk.Label(remaining_card, text=str(self.total_students), 
                                       font=('微软雅黑', 20, 'bold'), foreground='blue')
        self.remaining_label.pack(pady=(0, 5))
        
        # 点名显示区域
        display_frame = ttk.LabelFrame(main_frame, text="当前点名", padding="20")
        display_frame.pack(fill=tk.X, pady=15)
        
        self.name_label = ttk.Label(display_frame, text="准备就绪", 
                                   font=('微软雅黑', 54, 'bold'), foreground='#2c3e50')
        self.name_label.pack(pady=10)
        
        self.detail_label = ttk.Label(display_frame, text="", font=('微软雅黑', 14), foreground='#7f8c8d')
        self.detail_label.pack()
        
        # 按钮区域
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=15)
        
        # 按钮样式
        style = ttk.Style()
        style.configure('Accent.TButton', font=('微软雅黑', 11))
        
        self.roll_btn = ttk.Button(button_frame, text="🎲 开始滚动", 
                                   command=self.toggle_roll, width=15)
        self.roll_btn.pack(side=tk.LEFT, padx=5)
        
        self.pick_btn = ttk.Button(button_frame, text="✨ 随机抽取", 
                                   command=self.pick_one, width=15)
        self.pick_btn.pack(side=tk.LEFT, padx=5)
        
        self.reset_btn = ttk.Button(button_frame, text="🔄 重置记录", 
                                    command=self.reset_all, width=15)
        self.reset_btn.pack(side=tk.LEFT, padx=5)
        
        # 点名记录区域
        record_frame = ttk.LabelFrame(main_frame, text="📋 已点名记录", padding="10")
        record_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 创建表格
        columns = ('序号', '学号', '姓名', '班级')
        self.tree = ttk.Treeview(record_frame, columns=columns, show='headings', height=12)
        
        # 设置列标题和宽度
        column_widths = [80, 150, 100, 150]
        for col, width in zip(columns, column_widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor='center')
        
        # 添加滚动条
        scrollbar = ttk.Scrollbar(record_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 班级筛选
        filter_frame = ttk.Frame(main_frame)
        filter_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(filter_frame, text="班级筛选:").pack(side=tk.LEFT, padx=(0, 10))
        
        # 获取所有班级
        classes = sorted(set(s['班级'] for s in self.students))
        self.class_var = tk.StringVar(value="全部班级")
        
        class_combo = ttk.Combobox(filter_frame, textvariable=self.class_var, 
                                   values=["全部班级"] + classes, state="readonly", width=20)
        class_combo.pack(side=tk.LEFT)
        class_combo.bind('<<ComboboxSelected>>', self.filter_by_class)
    
    def toggle_roll(self):
        """切换滚动点名状态"""
        if not self.remaining_students:
            messagebox.showinfo("提示", "所有学生都已点过名了！点击'重置记录'重新开始。")
            return
            
        if self.is_rolling:
            self.is_rolling = False
            self.roll_btn.config(text="🎲 开始滚动")
            if self.current_student:
                self.show_student(self.current_student)
        else:
            self.is_rolling = True
            self.roll_btn.config(text="⏹️ 停止滚动")
            self.roll()
    
    def roll(self):
        """滚动显示学生姓名"""
        if self.is_rolling and self.remaining_students:
            self.current_student = random.choice(self.remaining_students)
            self.name_label.config(text=self.current_student['姓名'])
            self.detail_label.config(text=f"{self.current_student['班级']}")
            self.root.after(100, self.roll)
    
    def pick_one(self):
        """随机抽取一名学生"""
        if not self.remaining_students:
            messagebox.showinfo("提示", "所有学生都已点过名了！点击'重置记录'重新开始。")
            return
        
        # 如果正在滚动，先停止
        if self.is_rolling:
            self.is_rolling = False
            self.roll_btn.config(text="🎲 开始滚动")
        
        # 随机抽取
        student = random.choice(self.remaining_students)
        self.show_student(student)
        self.add_to_called(student)
    
    def show_student(self, student):
        """显示学生信息"""
        self.name_label.config(text=student['姓名'])
        self.detail_label.config(text=f"{student['班级']} | 学号：{student['学号']}")
        self.current_student = student
    
    def add_to_called(self, student):
        """添加到点名记录"""
        if student not in self.called_students:
            self.called_students.append(student)
            self.remaining_students.remove(student)
            self.update_record_table()
            self.update_stats()
    
    def reset_all(self):
        """重置所有记录"""
        self.called_students = []
        self.reset_remaining()
        self.current_student = None
        self.update_record_table()
        self.update_stats()
        self.name_label.config(text="准备就绪")
        self.detail_label.config(text="")
        if self.is_rolling:
            self.is_rolling = False
            self.roll_btn.config(text="🎲 开始滚动")
    
    def filter_by_class(self, event=None):
        """按班级筛选显示记录"""
        selected_class = self.class_var.get()
        self.update_record_table(selected_class)
    
    def update_record_table(self, class_filter=None):
        """更新记录表格"""
        # 清空现有记录
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # 添加新记录（可选择按班级筛选）
        for student in self.called_students:
            if class_filter == "全部班级" or class_filter is None or student['班级'] == class_filter:
                self.tree.insert('', tk.END, values=(
                    student['序号'],
                    student['学号'],
                    student['姓名'],
                    student['班级']
                ))
    
    def update_stats(self):
        """更新统计信息"""
        called_count = len(self.called_students)
        remaining_count = len(self.remaining_students)
        self.called_label.config(text=str(called_count))
        self.remaining_label.config(text=str(remaining_count))

def main():
    root = tk.Tk()
    app = RollCallApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()