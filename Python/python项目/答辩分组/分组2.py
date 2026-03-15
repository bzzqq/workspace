import random

# 指导老师和学生名单
teachers = ["Teacher1", "Teacher2", "Teacher3", "Teacher4", "Teacher5", "Teacher6", "Teacher7", "Teacher8", "Teacher9", "Teacher10"]
students = ["Student1", "Student2", "Student3", "Student4", "Student5", "Student6", "Student7", "Student8", "Student9", "Student10",
            "Student11", "Student12", "Student13", "Student14", "Student15", "Student16", "Student17", "Student18", "Student19", "Student20",
            "Student21", "Student22", "Student23", "Student24", "Student25", "Student26", "Student27", "Student28", "Student29", "Student30",
            "Student31", "Student32", "Student33", "Student34", "Student35", "Student36", "Student37", "Student38", "Student39", "Student40",
            "Student41", "Student42", "Student43", "Student44", "Student45", "Student46", "Student47", "Student48", "Student49", "Student50",
            "Student51", "Student52", "Student53", "Student54", "Student55", "Student56", "Student57", "Student58", "Student59", "Student60",
            "Student61", "Student62", "Student63", "Student64", "Student65", "Student66", "Student67", "Student68", "Student69", "Student70",
            "Student71", "Student72", "Student73", "Student74", "Student75", "Student76", "Student77", "Student78", "Student79", "Student80",
            "Student81", "Student82", "Student83", "Student84", "Student85", "Student86", "Student87", "Student88", "Student89", "Student90",
            "Student91", "Student92", "Student93", "Student94", "Student95", "Student96", "Student97", "Student98", "Student99", "Student100"]

# 随机排序学生名单和老师名单
random.shuffle(students)
random.shuffle(teachers)

# 每个答辩组的老师数量
teachers_per_group = 2

# 每个老师的指导学生数量
students_per_teacher = 10

# 计算答辩组的数量
num_groups = len(teachers) // teachers_per_group

# 分组字典，键为答辩组编号，值为对应答辩组的老师列表和学生列表
groups = {group_num: {"teachers": [], "students": []} for group_num in range(1, num_groups + 1)}

# 按老师的指导学生数量进行分组
for i in range(0, len(teachers), teachers_per_group):
    group_num = i // teachers_per_group + 1
    teacher_list = teachers[i:i + teachers_per_group]
    student_list = students[:teachers_per_group * students_per_teacher]
    students = students[teachers_per_group * students_per_teacher:]
    groups[group_num]["teachers"] = teacher_list
    groups[group_num]["students"] = student_list

# 检查学生是否在指导老师所在的组，并进行调整
for group_num, group_data in groups.items():
    teachers_in_group = group_data["teachers"]
    students_in_group = group_data["students"]
    for teacher in teachers_in_group:
        students_to_swap = []
        for student in students_in_group:
            if student in groups[group_num]["teachers"]:
                students_to_swap.append(student)
        for student in students_to_swap:
            students_in_group.remove(student)
            random_group_num = random.choice(list(groups.keys()))
            while student in groups[random_group_num]["teachers"] or student in groups[random_group_num]["students"]:
                random_group_num = random.choice(list(groups.keys()))
            groups[random_group_num]["students"].append(student)

# 输出分组结果

for group_num, group_data in groups.items():
    print(f"Group {group_num}:")
    print("Teachers:", group_data["teachers"])
    print("Students:", group_data["students"])
    print()
