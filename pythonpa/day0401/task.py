import requests
import re


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
url = 'http://sports.163.com/zc/'

req = requests.get(url, headers)
ls = req.text
print(ls)


