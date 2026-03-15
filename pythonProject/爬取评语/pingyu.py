# import requests

# url = 'https://mobilelearn.chaoxing.com/page/renwuNew/personalScoreOnlyRead_new?activeId=5000097587745&groupId=5000003889411&targetUid=292168063&classId=99092890&courseId=243425036&isTeacherViewOpen=1&fid=0'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
# response = requests.get(url, headers=headers, auth=('15920464144', 'hbnd003120'))

# if response.status_code == 200:
#     print(response.text)
# else:
#     print(f'Failed to get webpage: Status Code {response.status_code}')

from pythonProject.爬取评语.ff import webdriver

# 创建Chrome浏览器对象
browser = webdriver.Chrome()
# 加载指定的页面
browser.get('https://www.baidu.com/')