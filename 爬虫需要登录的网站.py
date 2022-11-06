# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 06:38:09 2022

@author: Master Zhang
"""
import requests
from bs4 import BeautifulSoup
url = 'https://i.csdn.net/#/user-center/profile?spm=1001.2014.3001.5516'

r = requests.get(url,timeout=30)
r.encoding = r.apparent_encoding

r.text
soup = BeautifulSoup(r.text,"html.parser")

r.request.headers['Content-Type']

r.raise_for_status

r.request.headers
r.headers














# 点击提交按钮
wd.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
# 等5秒
time.sleep(5)
# 关闭页面
wd.quit()














