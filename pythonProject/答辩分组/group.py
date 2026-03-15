# import random

# def assign_groups(students):
#     random.shuffle(students)  # 随机打乱学生名单

#     # num_groups = len(students) // 6  # 计算需要的组数量
#     num_groups = 6
#     groups = [[] for _ in range(num_groups)]  # 初始化组列表

#     for student in students:
#         group_assigned = False  # 标记学生是否已经被分组

#         while not group_assigned:
#             group_index = random.randint(0, num_groups - 1)  # 随机选择一个组

#             # 检查学生是否满足分组要求
#             if ((student == ['张三', 'M', '45'] and group_index != 0) or
#                 (student == ['张三1', 'M1', '451'] and group_index != 1) or
#                 (student == ['张三3', 'M3', '453'] and group_index != 2) or
#                 (student == ['张三4', 'M4', '454'] and group_index != 3) or
#                 (student == ['张三5', 'M5', '455'] and group_index != 4) or
#                 (student == ['张三6', 'M6', '456'] and group_index != 5)):

#                 groups[group_index].append(student)
#                 group_assigned = True

#     return groups

# # 示例学生名单
# # students = [['张三', 'M', '45'], ['张三1', 'M1', '451'], ['张三3', 'M3', '453'], ['张三4', 'M4', '454'], ['张三5', 'M5', '455'], ['张三6', 'M6', '456']]
# students1 = ['张三', 'M', '45']
# students2 = ['张三1', 'M1', '451']
# students3 = ['张三3', 'M3', '453']
# students4 = ['张三4', 'M4', '454']
# students5 = ['张三5', 'M5', '455']
# students6 = ['张三6', 'M6', '456']

# # groups = assign_groups(students)

# # 输出学生分组
# for i, group in enumerate(groups):
#     print(f"组 {i+1}: {group}")
# # print(groups)

import random

num_groups = 6
groups = [[] for _ in range(num_groups)]  # 初始化组列表

students1 = ["赵炳权","杨文华","徐亚伟","王铭浠","倪欣雨","杨悦","吴晓迪","李梦翠","齐冰冉","李垚","路学敏","冯雪鹏","武韶博","孙晓科","任晓璇","张婉红","学生","雷璐婷","戎毅","李武波","王成","何加乐","陈贵雨","张念一","吕建国","陈鹤"]
students2 = ['张三1', 'M1', '451']
students3 = ['张三3', 'M3', '453']
students4 = ['张三4', 'M4', '454']
students5 = ['张三5', 'M5', '455']
students6 = ['张三6', 'M6', '456']

students_nums = len(students1) + len(students2) + len(students3) + len(students4) + len(students5) + len(students6)
students_per_group = students_nums // 6 + 1


random.shuffle(students1)  # 随机打乱学生名单
random.shuffle(students2)  # 随机打乱学生名单
random.shuffle(students3)  # 随机打乱学生名单
random.shuffle(students4)  # 随机打乱学生名单
random.shuffle(students5)  # 随机打乱学生名单
random.shuffle(students6)  # 随机打乱学生名单

for student in students1:
    group_assigned = False  # 标记学生是否已经被分组

    while not group_assigned:
        group_index = int(random.choice("12345"))  # 随机选择一个组
        if len(groups[group_index]) < students_per_group:
            groups[group_index].append(student)
            group_assigned = True


for student in students2:
    group_assigned = False  # 标记学生是否已经被分组

    while not group_assigned:
        group_index = int(random.choice("02345"))  # 随机选择一个组
        if len(groups[group_index]) < students_per_group:
            groups[group_index].append(student)
            group_assigned = True


for student in students3:
    group_assigned = False  # 标记学生是否已经被分组

    while not group_assigned:
        group_index = int(random.choice("01345"))  # 随机选择一个组
        if len(groups[group_index]) < students_per_group:
            groups[group_index].append(student)
            group_assigned = True


for student in students4:
    group_assigned = False  # 标记学生是否已经被分组

    while not group_assigned:
        group_index = int(random.choice("01245"))  # 随机选择一个组
        if len(groups[group_index]) < students_per_group:
            groups[group_index].append(student)
            group_assigned = True


for student in students5:
    group_assigned = False  # 标记学生是否已经被分组

    while not group_assigned:
        group_index = int(random.choice("01235"))  # 随机选择一个组
        if len(groups[group_index]) < students_per_group:
            groups[group_index].append(student)
            group_assigned = True


for student in students6:
    group_assigned = False  # 标记学生是否已经被分组

    while not group_assigned:
        group_index = int(random.choice("01234"))  # 随机选择一个组
        if len(groups[group_index]) < students_per_group:
            groups[group_index].append(student)
            group_assigned = True
# print(groups)

# 示例学生名单
# students = [['张三', 'M', '45'], ['张三1', 'M1', '451'], ['张三3', 'M3', '453'], ['张三4', 'M4', '454'], ['张三5', 'M5', '455'], ['张三6', 'M6', '456']]


# groups = assign_groups(students)

# 输出学生分组
for i, group in enumerate(groups):
    print(f"组 {i+1}: {group}")
# print(groups)

for i, group in enumerate(groups):
    print(f"组 {i+1}: {len(group)}")