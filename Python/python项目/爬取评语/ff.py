from selenium import webdriver
from selenium.webdriver.common.by import By


# 创建Chrome浏览器对象
browser = webdriver.Firefox()

# 加载指定的页面
browser.get('https://mobilelearn.chaoxing.com/page/renwuNew/personalScoreOnlyRead_new?activeId=5000097587745&groupId=5000003889411&targetUid=292168063&classId=99092890&courseId=243425036&isTeacherViewOpen=1&fid=0')

# 设置隐式等待时间为10秒
browser.implicitly_wait(10)

# 尝试查找元素
element = browser.find_element(By.CLASS_NAME, 'teacher-dec')

# # 获取页面源代码
# html = browser.page_source
# print(html)

# 提取评语
element1 = browser.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div/span[2]')

print(element1.text)

# 关闭浏览器
browser.close()
