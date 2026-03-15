def traverse(triangle):
    Row = len(triangle)
    mini = triangle[Row - 1]  # mini:最后一行的节点信息
    for i in range(Row - 2, -1, -1):  # 从倒第二行求起,因为底部那行的值已经定了
        j = 0  # 开始刷新第i行
        while j < sum([triangle[i][x] != 0 for x in range(Row)]):
            # 这行的真正(非零)长度
            mini[j] = triangle[i][j] + min(mini[j], mini[j + 1])
            # 上面那行很妙啊,mini[0]变成倒第二行的成品了,却不影响后边的计算
            j += 1
    return mini[0]


triangle = [[9, 0, 0, 0, 0], [12, 15, 0, 0, 0], [10, 6, 8, 0, 0], [2, 18, 9, 5, 0], [19, 7, 10, 4, 16]]
print(traverse(triangle))
