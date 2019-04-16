import requests

from bs4 import BeautifulSoup
import pymongo
import re

def ua_url(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

    reapose = requests.get(url, headers)
    html = reapose.content
    return html

