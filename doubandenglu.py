import cv2
from selenium import webdriver
import requests
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
while True:
    #1. 显示滑动验证码
    driver.get('https://www.douban.com/')
    driver.implicitly_wait(10)
    sleep(3)
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="anony-reg-new"]/div/div[1]/iframe'))
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/ul[1]/li[2]').click()
    driver.find_element(By.XPATH,"//*[@id='username']").send_keys("13091448108")
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("jjyu119511")
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
    sleep(2)
    #2. 获取到滑块以及滑板到图片地址
    
    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div[7]/iframe'))
    ##2.1 滑块
    slideBlock = driver.find_element(By.XPATH,'/html/body/div/div[3]/div[2]/div[7]')
    slideBlock_url = "https://t.captcha.qq.com/cap_union_new_getcapbysig?img_index=0&image=02790500000000430000000bb9480baa2d4b&sess=s0aI5mubpzs43_i-Kc56jRszrxZTBuh8SGxzRDLWsDqY1eXQTztj-SRyjM5-Z5zbA7H5CnJlwo03feBauq_cuobpaMFXGQIKG_kYR4DcC5EDq2ciUzDMdThql5SJs_iAdiyJVioKEXsvEWAQTb6Mt8ZHKbywABpYZS2izT7qioWhG9lrRGqyPONvOH0YijPmzFa_XmuBhdyhLUeHh5GJCxkVefVE8WTeea1sJGFg3VPFlQKg_HnaydIa5ZwpkVLnx2v4K4nf6Fz3PjA1u5row7nWqjpD3Xw9JPSl1ik-iqaetxrHxfzOuAnfBFb9OAGitbuhzkT9Zj7zgtgpxoLaLwYtiNUQIcG-fVfVrOX27qyB1MvZNBlggIFyoKSmz0FkkBHt54kM8LFYfrzDFKdgjWiI0xzYEsUVtyY9agCMbg7argfE4hZrKgOg**"
    
    ##2.2 滑板
    slideBg = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div[8]')
    slideBg_url = "https://t.captcha.qq.com/cap_union_new_getcapbysig?img_index=1&image=02790500000000430000000bb9480baa2d4b&sess=s0aI5mubpzs43_i-Kc56jRszrxZTBuh8SGxzRDLWsDqY1eXQTztj-SRyjM5-Z5zbA7H5CnJlwo03feBauq_cuobpaMFXGQIKG_kYR4DcC5EDq2ciUzDMdThql5SJs_iAdiyJVioKEXsvEWAQTb6Mt8ZHKbywABpYZS2izT7qioWhG9lrRGqyPONvOH0YijPmzFa_XmuBhdyhLUeHh5GJCxkVefVE8WTeea1sJGFg3VPFlQKg_HnaydIa5ZwpkVLnx2v4K4nf6Fz3PjA1u5row7nWqjpD3Xw9JPSl1ik-iqaetxrHxfzOuAnfBFb9OAGitbuhzkT9Zj7zgtgpxoLaLwYtiNUQIcG-fVfVrOX27qyB1MvZNBlggIFyoKSmz0FkkBHt54kM8LFYfrzDFKdgjWiI0xzYEsUVtyY9agCMbg7argfE4hZrKgOg**"

    #print(slideBg_url)
    #print(slideBlock_url)

    #3. 下载滑块和滑板
    with open('images/big_images.jpg','wb') as f:
        f.write(requests.get(slideBg_url).content)
        f.close()

    with open('images/small_images.jpg','wb') as f:
        f.write(requests.get(slideBlock_url).content)
        f.close()

    #4. 智能匹配滑块和滑板的小图重叠后x的距离
    big_grag = cv2.imread("images/big_images.jpg",0) # 以灰度模式加载图片
    small_grag = cv2.imread("images/small_images.jpg",0) # 以灰度模式加载图片)
    res = cv2.matchTemplate(big_grag,small_grag,cv2.TM_CCORR_NORMED) #匹配对象
    cv2.imread
    value = cv2.minMaxLoc(res)
    print("value的值",value)
    x = value[2][0]
    print(x)

    #5. 缩放比例以及校准滑块偏移量，原图是680*390，实际是282*162
    x = int(x*282/680)
    py = 31 - int(20*282/680)
    x = x-py
    print(x)

    #6. 通过ActionChains滑动解锁
    hk_ele = driver.find_element(By.XPATH,'/html/body/div/div[3]/div[2]/div[7]')
    action = ActionChains(driver) # 初始化一个鼠标对象
    action.click_and_hold(hk_ele).perform()  #鼠标按住不动
    action.drag_and_drop_by_offset(hk_ele,145,0).perform() #把滑动移动到指定的坐标，0代表纵坐标
    sleep(3)

    ## 如果元素不存在，则表示成功
    #7. 滑动失败后增加重试机制
    try:
        driver.find_element(By.XPATH,'//*[@id="captcha_close"]/div')
    except Exception as e:
        break
