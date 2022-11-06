# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 07:07:32 2022

@author: Master Zhang
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
from selenium.webdriver.common.by import By

# 加载谷歌浏览器驱动
wd = webdriver.Chrome(service=Service(r'F:\work\python\python_location2\chromedriver.exe'))

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('http://192.168.20.112:8092')

# 等5秒
time.sleep(5)

# 全屏显示
wd.maximize_window()

# 设置账号
# wd.find_element(By.ID, 'userName').send_keys('delete')
# 设置密码
# wd.find_element(By.ID, 'password').send_keys('456789')
# 设置验证码
# wd.find_element(By.NAME, 'code').send_keys('1111')
# 点击提交按钮
# wd.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
# 通过xpath获取账号输入框位置
userName = wd.find_element(By.XPATH,
                           '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/form/div[1]/div/input')
# 通过xpath获取密码输入框位置
password = wd.find_element(By.XPATH,
                           '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/form/div[2]/div/input')
# 通过xpath获取验证码的输入框位置
code = wd.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/form/div[3]/div[1]/input')
# 通过xpath获取按钮的位置
button = wd.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/form/div[4]/button')

# 账号输入框输入账号
userName.send_keys('delete')
# 密码输入框中输入密码
password.send_keys('456789')
# 验证码输入框中输入验证码
code.send_keys('123')
# 点击按钮
button.click()

# 等5秒
time.sleep(5)
# 验证是否登陆成功
login_success = wd.find_element(By.XPATH, '/html/body/div[1]/ul[2]/li[3]/a/div').text
print(login_success)
# 断言验证真实姓名
assert  login_success == 'delete1'

# 等5秒
time.sleep(3)

# 关闭页面
wd.quit()
# =============================================================================
# https://blog.csdn.net/weixin_54767527/article/details/125782752
# https://blog.csdn.net/weixin_42182599/article/details/125895385
# https://blog.csdn.net/weixin_35568959/article/details/112542705
# 获取图片的另一种方法：
# https://blog.csdn.net/zhangmaoyang66/article/details/123240873
# =============================================================================


import cv2
import time
from selenium import webdriver
import requests
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#1. 显示滑动验证码
driver.get('https://www.douban.com/')
driver.maximize_window()
driver.implicitly_wait(10)
sleep(3)
driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/iframe'))
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/ul[1]/li[2]').click()
driver.find_element(By.XPATH,"//*[@id='username']").send_keys("13091448108")
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("jjyu119511")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
sleep(2)
#2. 获取到滑块以及滑板到图片地址

driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[7]/iframe'))

sleep(1)
# 重新获取滑块的 xpath
hk_ele = driver.find_element(By.XPATH,'/html/body/div/div[3]/div[2]/div[6]')
action = ActionChains(driver) # 初始化一个鼠标对象
action.click_and_hold(hk_ele).perform()  #鼠标按住不动
action.drag_and_drop_by_offset(hk_ele,150,0).perform() #把滑动移动到指定的坐标，0代表纵坐标
sleep(3)














