from selenium import webdriver

# http://sports.sina.com.cn/
# http://tech.163.com/
sta = webdriver.PhantomJS()
url = 'http://sports.sina.com.cn/'
sta.get(url)
con = sta.find_elements_by_class_name('ty-card-tt')

print(con)