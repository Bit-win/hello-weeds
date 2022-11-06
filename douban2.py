import cv2
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
 
driver = webdriver.Chrome()
driver.get("https://www.douban.com/")
driver.maximize_window()
 
iframe = driver.find_element(By.CSS_SELECTOR, "#anony-reg-new > div > div.login > iframe")
driver.switch_to.frame(iframe)

phone = driver.find_element(By.CSS_SELECTOR,
                            "body > div.account-body.login-wrap.login-start.account-anonymous > div.account-tabcon-start > div.account-form > div:nth-child(3) > div > input")
phone.send_keys('13091448108')
time.sleep(1)
slider_ = driver.find_element(By.CSS_SELECTOR,
                              'body > div.account-body.login-wrap.login-start.account-anonymous > div.account-tabcon-start > div.account-form > div:nth-child(4) > div > div > a')
slider_.click()
time.sleep(3)
iframe = driver.find_element(By.XPATH,'/html/body/div[7]/iframe')
driver.switch_to.frame(iframe)
while True:
    # 1、获取滑块及滑板地址
    src = driver.find_element(By.XPATH,'/html/body/div/div[3]/div[2]/div[7]')
    bug_src_url = "https://t.captcha.qq.com/cap_union_new_getcapbysig?img_index=0&image=02790500000000430000000bb9480baa2d4b&sess=s0aI5mubpzs43_i-Kc56jRszrxZTBuh8SGxzRDLWsDqY1eXQTztj-SRyjM5-Z5zbA7H5CnJlwo03feBauq_cuobpaMFXGQIKG_kYR4DcC5EDq2ciUzDMdThql5SJs_iAdiyJVioKEXsvEWAQTb6Mt8ZHKbywABpYZS2izT7qioWhG9lrRGqyPONvOH0YijPmzFa_XmuBhdyhLUeHh5GJCxkVefVE8WTeea1sJGFg3VPFlQKg_HnaydIa5ZwpkVLnx2v4K4nf6Fz3PjA1u5row7nWqjpD3Xw9JPSl1ik-iqaetxrHxfzOuAnfBFb9OAGitbuhzkT9Zj7zgtgpxoLaLwYtiNUQIcG-fVfVrOX27qyB1MvZNBlggIFyoKSmz0FkkBHt54kM8LFYfrzDFKdgjWiI0xzYEsUVtyY9agCMbg7argfE4hZrKgOg**"
    src = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div[8]')
    small_src_url = "https://t.captcha.qq.com/cap_union_new_getcapbysig?img_index=1&image=02790500000000430000000bb9480baa2d4b&sess=s0aI5mubpzs43_i-Kc56jRszrxZTBuh8SGxzRDLWsDqY1eXQTztj-SRyjM5-Z5zbA7H5CnJlwo03feBauq_cuobpaMFXGQIKG_kYR4DcC5EDq2ciUzDMdThql5SJs_iAdiyJVioKEXsvEWAQTb6Mt8ZHKbywABpYZS2izT7qioWhG9lrRGqyPONvOH0YijPmzFa_XmuBhdyhLUeHh5GJCxkVefVE8WTeea1sJGFg3VPFlQKg_HnaydIa5ZwpkVLnx2v4K4nf6Fz3PjA1u5row7nWqjpD3Xw9JPSl1ik-iqaetxrHxfzOuAnfBFb9OAGitbuhzkT9Zj7zgtgpxoLaLwYtiNUQIcG-fVfVrOX27qyB1MvZNBlggIFyoKSmz0FkkBHt54kM8LFYfrzDFKdgjWiI0xzYEsUVtyY9agCMbg7argfE4hZrKgOg**"
    # 2、下载到本地图片
    with open("images/big_srs.jpg", "wb") as f:
        f.write(requests.get(bug_src_url).content)
        
    with open("images/small_srs.jpg", "wb") as f:
        f.write(requests.get(small_src_url).content)
    # print(bug_src_url)
    # print(small_src_url)
    # 3、图片识别，匹配滑块验证码的距离，滑块和滑板的小图重叠后x轴的距离
    # (0.5932352542877197, 0.8350041508674622, (486, 53), (172, 155))
    big = cv2.imread("images//big_srs.jpg", 0)  # 以灰度方式加载图片
    small = cv2.imread("images//small_srs.jpg", 0)  # 以灰度方式加载图片
    res = cv2.matchTemplate(big, small, cv2.TM_CCORR_NORMED)  # 匹配模式        小图在大图中的位置
    value_num = cv2.minMaxLoc(res)  # 匹配小图和大图最左边和最右边的位置
    print(value_num)
    x = value_num[2][0]  # 横坐标
    # 4、缩放比例及校准滑块偏移量。原图680x390，实际页面图283x162
    print(x)
    x = int(x * 283 / 680)  # 缩放比例
    print(x)
    bk = 30 - int(20 * 283 / 680)  # 偏移量
    print(bk)
    x = x - bk
    print(x)
    # 6、通过ActionChains滑动解锁
    action = ActionChains(driver)
    action.click_and_hold(src).perform()  # 鼠标左键按下不放
    # action.drag_and_drop_by_offset(src,x,0).perform()   # 滑块滑动到指定坐标
    action.move_by_offset(x, 0)  # 需要滑动的坐标
    action.release().perform()  # 释放鼠标
    try:
        driver.find_element(By.CSS_SELECTOR, "#tcStatus > div.tc-status--right.table-wrap > div:nth-child(2)")
    except:
        break
time.sleep(5)
driver.quit()