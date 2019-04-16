# import requests
#
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
# }
# url = 'https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f810000bhsudsmm7dkrnkrdi5m0&amp;line=0'
#
# respone = requests.get(url=url, headers=headers)
# re = respone.content
# print(re)
#
#
# with open('./shiping/shiping.mp4', 'wb')as f:
#     f.write(re)

import requests
import json

headers = {'User-Agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.2; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10)'}
url = 'http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&' \
      'app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&' \
      'cuid=C6B21AEA754F43116FAA0285FBE7E281&ovr=4.4.2&device=samsung_SM-G955N&net_type=1&' \
      'client_id=lKN8XwWdHBE873WeXh%2BZzg%3D%3D&info_ms=y1W6rBWLOAkiADI4uJYI6A%3D%3D&info_ma=yyTGCWjKkMnvtgYBct6oYsNbosIUlr4xvwN%2FfpY2q0c%3D&mno=0&info_la=0UUdN52XBwrMFqiZgf2Q2Q%3D%3D&info_ci=0UUdN52XBwrMFqiZgf2Q2Q%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=yyTGCWjKkMnvtgYBct6oYsNbosIUlr4xvwN%2FfpY2q0c%3D&os_level=19&os_id=408d5c0655ec1515&resolution=720_1280&dpi=240&client_ip=172.17.100.15&pdunid=c0655ec1515408d5'
response = requests.get(url, headers=headers)
data = response.text
# print(data)
data = json.loads(data)['list']
for item in data:
    name = item['name']
    cover = item['cover']
    print('英雄', name)
    print('图片', cover)


