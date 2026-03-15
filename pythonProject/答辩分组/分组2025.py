import random
import pandas as pd

# 读取Excel文件
df = pd.read_excel('师生双选信息表2025.xlsx')

# 创建一个字典来存储老师和学生之间的关系
teacher_students = {teacher: [] for teacher in df['指导教师'].unique()}

# 填充字典
for index, row in df.iterrows():
    teacher_students[row['指导教师']].append(row['学号'])

# 输出字典内容
# for teacher, students in teacher_students.items():
#     print(f"{teacher}: {students}")

# 现在你可以使用这个字典来进行答辩分组的操作

# 答辩组
groups = {
    "1组": ["马晶军", "李现", "赵丽丽", "张斌"],
    "2组": ["周欣", "刘红蕾", "高贵"],
    "3组": ["许国贺", "陈明珠", "闫思琦"],
    "4组": ["刘祺凤", "孙燕芳", "代瑞慧"],
    "5组": ["王林艳", "芦爽", "付美臻"],
    "6组": ["张力红", "李继文", "石田"],
    "7组": ["周晓斐", "纪晓婧", "彭丹丹"],
    "8组": ["马晶军", "高建平", "郭利静", "刘莎莎"],
}

# 分配学生到答辩组
# assigned_students = {"1组": [], "2组": [], "3组": [], "4组": [], "5组": [], "6组": [], "7组": [], "8组": []}
assigned_students = {f"{i}组": [] for i in range(1, 9)}

# 将学生分配到不是自己指导老师的答辩组
for teacher, students in teacher_students.items():
    for student in students:
        # 随机选择一个不是学生指导老师的答辩组
        possible_groups = [g for g in groups if teacher not in groups[g]]
        if possible_groups:
            group = random.choice(possible_groups)
            assigned_students[group].append(student)


for group in assigned_students:
    print(group)
# 尝试平衡每个组的学生数量
max_attempts = 100  # 设置最大尝试次数以避免无限循环
for attempt in range(max_attempts):
    group_sizes = [len(students) for students in assigned_students.values()]
    if max(group_sizes) - min(group_sizes) <= 2:
        break  # 如果已经平衡或差异很小，则停止
    for group in assigned_students:
        if len(assigned_students[group]) > 36:
            # 移动一个学生到另一个组
            student_to_move = assigned_students[group].pop()
            # 找到学生数量最少的组，并确保学生指导老师不在该组
            target_group = min([g for g in assigned_students if teacher_students[df[df['学号'] == student_to_move]['指导教师'].values[0]] not in groups[g]], key=assigned_students.get)
            assigned_students[target_group].append(student_to_move)
print(group_sizes)
# 输出分配结果
for group, students in assigned_students.items():
    print(f"{group}: {students}")

# 创建DataFrame来存储结果
results_df = pd.DataFrame({
    '答辩组': [],
    '学号': [],
    '指导教师': []
})

# 将结果添加到DataFrame
for group, students in assigned_students.items():
    for student in students:
        new_row = pd.DataFrame({'答辩组': group, '学号': student, '指导教师': df[df['学号'] == student]['指导教师'].values[0]}, index=[0])
        results_df = pd.concat([results_df, new_row], ignore_index=True)

# 输出结果到Excel文件
results_df.to_excel('答辩分组结果2025.xlsx', index=False)

print("答辩分组结果已输出到Excel文件。")