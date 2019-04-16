# level 1:
# 1、阅读课件
# 2、掌握单个元素的查找方法
# 3、掌握多个元素的查找方法
# 4、元素id，位置，尺寸，属性，文本的获取方法
#
# 案例：网易科技频道爬虫
# http://tech.163.com/
# 爬取新闻标题，链接
#
# 导入webdriver

'''
from selenium import webdriver
# 创建浏览器对象
sta = webdriver.Chrome()
url = 'http://tech.163.com/'
sta.get(url)
hhh = sta.find_elements_by_css_selector("div.data_row.news_article.clearfix")
# print(hhh)
for i in hhh:
    s = i.find_element_by_css_selector('h3>a').text
    u = i.find_element_by_css_selector('h3>a').get_attribute('href')
    print(s)
    print(u)
    print()
# url = sta.find_elements_by_xpath('//div[@class="news_title"]/h3/a')
sta.close()
sta.quit()
'''

#
# 案例：模拟登陆微博
# http://www.weibo.com/login.php
from selenium import webdriver
import time
'''
name ='3414018462@qq.com'
password = 'qikuedu9527'
def login():
    web = webdriver.Chrome()
    try:
        web.maximize_window()
        web.get('http://www.weibo.com/login.php')
        time.sleep(2)
        
        print('输入用户名....')
        web.find_element_by_id('loginname').clear()  # 清除输入框中默认的内容
        web.find_element_by_id('loginname').send_keys(name)
        time.sleep(2)
    
        print('输入密码....')
        web.find_element_by_name('password').clear()
        web.find_element_by_name('password').send_keys(password)
        time.sleep(2)

        web.find_element_by_xpath('//div[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
        time.sleep(3)
        print(web.current_url)
        print(web.page_source)
        print('登陆成功.')
        time.sleep(10)
        web.close()
    except Exception as e:
        print('登陆失败'+e)


if __name__ == '__main__':
    login()
    
'''

# 案例：微博信息的爬取
# 模拟登录后，爬取王思聪的官方微博
# https://weibo.com/p/1003061826792401?is_all=1
# 提取用户名，微博内容，发表时间
#
'''
from selenium import webdriver

import time
sta = webdriver.Chrome()
def login():

    try:
        sta.maximize_window()
        sta.get('http://www.weibo.com/login.php')
        time.sleep(2)

        print('输入用户名....')
        sta.find_element_by_id('loginname').clear()  # 清除输入框中默认的内容
        sta.find_element_by_id('loginname').send_keys(loginname)
        time.sleep(2)

        print('输入密码....')
        sta.find_element_by_name('password').clear()
        sta.find_element_by_name('password').send_keys(password)
        time.sleep(2)

        sta.find_element_by_xpath('//div[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
        time.sleep(2)
        # print(driver.current_url)
        # print(driver.page_source)
        print('登陆成功.')
        time.sleep(5)
        return sta
    except Exception as e:
        print('登陆失败'+ e)


def request(url):
    sta.get(url)
    end_height = sta.execute_script('return document.body.scrollHeight')
    while True:
        sta.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)
        new_height = sta.execute_script('return document.body.scrollHeight')
        # print(end_height, new_height)
        if new_height == end_height:
            break
        end_height = new_height
    time.sleep(3)
    return sta


def spider(sta):
    BASE_URL = 'https://weibo.com'
    div =sta.find_elements_by_class_name('WB_detail')
    print(len(div))
    for d in div:
        print('='*100)
        title = d.find_element_by_css_selector('.WB_info > a').text
        print('title:', title)
        times = d.find_element_by_css_selector('.WB_from.S_txt2 > a').text
        print('times:', times)
        try:
            content = d.find_element_by_css_selector('.WB_text.W_f14').text
        except:
            content = '无'
        print('content:', content)
    # 下一页
    a_href = sta.find_element_by_link_text('下一页').get_attribute('href')
    print(a_href, type(a_href))
    sta = request(BASE_URL+a_href)
    spider(sta)


if __name__ == '__main__':
    sta = webdriver.Chrome()
    loginname = '3414018462@qq.com'
    password = 'qikuedu9527'
    URL = 'https://weibo.com/p/1003061826792401?is_all=1'
    login()
    sta = request(URL)
    spider(sta)
'''

# 案例：新浪体育爬虫
# http://sports.sina.com.cn/
# 向下拉动滚动条3次，
# 爬取新闻标题，链接
'''
from selenium import webdriver
import time

def request(url):
    sta = webdriver.Chrome()
    sta.get(url)
    for i in range(3):
        sta.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)
    return sta


def spider(rev):
    h3 = rev.find_elements_by_class_name('ty-card-tt')
    for h in h3:
        print('='*100)
        title = h.find_element_by_tag_name('a').text
        print('title:', title)
        href = h.find_element_by_tag_name('a').get_attribute('href')
        print('href:', href)


if __name__ == '__main__':
    URL = 'http://sports.sina.com.cn/'
    rev = request(URL)
    spider(rev)
'''

# 案例：大众点评酒店信息爬取
# url:http://www.dianping.com/shanghai/hotel/g3020p1
# 爬取酒店名称、位置，价格
#

'''
sta = webdriver.Chrome()
n=1
while n<=16:
    url = 'http://www.dianping.com/shanghai/hotel/'+ 'g3020p%s'%n
    n = n + 1
    sta.get(url)
    uu = sta.find_elements_by_css_selector('div.hotel-info-ctn')
    for i in uu:
        t = i.find_element_by_css_selector('div>h2>a').text
        w = i.find_element_by_css_selector('p.place').text
        u = i.find_element_by_css_selector('div.hotel-remark>div>p').text
        p = i.find_element_by_css_selector('p.hotel-tags').text
        print("酒店名称：", t)
        print("酒店位置:", w)
        print("酒店优点:", p)
        print("价钱：", u)
        print("="*50)
sta.close()
sta.quit()

'''

# level 2:
#
# 案例：斗鱼直播平台爬虫
# https://www.douyu.com/directory/all
# 爬取房间名称，主播名称，在线人数
#
#
# 案例：京东爬虫
# https://www.jd.com/
# 打开京东页面，搜索栏中输入“手机”,
# 滚动条拉到底部请求三次
# 爬取商品名称及价格

# webdriver.Chrome()
# url = 'https://www.jd.com/'
