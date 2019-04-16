import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
             'Cookie': 'pgv_pvi=9048994816; pgv_si=s8165804032; _qpsvr_localtk=0.0426686469814086; ptisp=ctc; '
                       'RK=HNaNEX64Xq; ptcz=15394cca0d9e8bd18590797ed15b708ea00a8ad0ac0791acbbe7f3fce060961a; '
                       'pgv_info=ssid=s2749850365; pgv_pvid=136612141; ts_uid=4760984024; pac_uid=0_7c2eb5d8a2ee3; '
                       'ts_last=www.qq.com/; ad_play_index=99;'
                       ' ptcz=15394cca0d9e8bd18590797ed15b708ea00a8ad0ac0791acbbe7f3fce060961a; fp3_id1=1100BB2D5E9BA027E53A310B'
                       'AF6BAB28B8325E28E37BE32C4568910FCA89278E91A7AF440043F5814DB1AC45BDF433FCBF0F'}
requests = requests.get('https://www.qq.com/', headers=headers)
print(requests.text)


with open("qq.html", "w", encoding="utf-8") as file:
    file.write(requests.text)

