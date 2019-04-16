import requests
import random

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Open():
    def __init__(self,username,password) -> None:
        self.url = 'https://passport.bilibili.com/login'
        self.llq = webdriver.Chrome()
        self.weat =WebDriverWait(self.llq, 50)
        self
