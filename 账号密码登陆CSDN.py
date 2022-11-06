# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 22:15:36 2022

@author: Master Zhang
"""
###账号密码登陆CSDN

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True
# 屏蔽inforbar
edge_options.add_experimental_option('useAutomationExtension', False)
edge_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
# 创建driver
wd = webdriver.Edge(executable_path='I:\python3.8\MicrosoftWebDriver.exe', options=edge_options)

# =============================================================================
# option = webdriver.Edge(service=Service(r'I:\python3.8\MicrosoftWebDriver.exe'))
# option.add_argument('disable-infobars')
# option.add_experimental_option("excludeSwitches", ['enable-automation'])#真正起作用的是这段
# wd = webdriver.Chrome(options=option,desired_capabilities = None)
# =============================================================================

# =============================================================================
# option = webdriver.ChromeOptions()
# option.add_argument('disable-infobars')
# option.add_experimental_option("excludeSwitches", ['enable-automation'])#真正起作用的是这段
# wd = webdriver.Chrome(options=option,desired_capabilities = None)
# =============================================================================



# 创建 WebDriver 对象，指明使用chrome浏览器驱动
# wd = webdriver.Edge(service=Service(r'I:\python3.8\MicrosoftWebDriver.exe'))



# # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.douban.com/')

# 等5秒
time.sleep(3)
# 全屏显示
wd.maximize_window()


# 通过xpath获取按钮的位置
# =============================================================================
# button = wd.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div/div[1]/a')
# button.click()
# # 等5秒
# time.sleep(2)
# =============================================================================


wd.switch_to.default_content()
wd.switch_to.frame(wd.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/iframe'))
# button = wd.find_element(By.XPATH,('//*[@id = "sortable"]/li[4]'))


button = wd.find_element(By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[2]')

button.click()

# 等5秒
time.sleep(2)
# 通过xpath获取账号输入框位置
userName = wd.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[3]/div/input')
# 通过xpath获取密码输入框位置
password = wd.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[4]/div/input')

# 账号输入框输入账号
userName.send_keys('13091448108')
# 密码输入框中输入密码
password.send_keys('jjyu119511')

button = wd.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[5]/a')
# 等5秒
time.sleep(1)
# 点击按钮
button.click()

