# level 1:
# 1、招聘爬虫（scrapy）
# https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?
# lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&
# jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&
# address=&line=&specialarea=00&from=&welfare=
# 搜索python，爬取职位名称，公司，工作地点，薪资，发布时间
# 能控制爬取的页数，城市
# 设置不同的pipeline，保存到zhaopin.csv文件，保存到mysql
#



# level 2：
# 2、阳光热线问政平台（spider）
# http://wz.sun0769.com/index.php/question/questionType?type=4&page=
# 爬去投诉帖子的标题，编号，链接，内容，投诉者，投诉时间
# 存储到mysql数据库
#


# 3、腾讯招聘（scrapy）
# http://hr.tencent.com/position.php?&start=0#a
# 爬取招聘岗位，城市，类别，人数，发布日期
#
# 3、b站排行榜爬虫（scrapy）
# https://www.bilibili.com/ranking#!/all/0/0/7/
# 爬取编号，标题，url，综合评分，播放量，评论数
# 存储到mysql数据库
#
#
#
#
