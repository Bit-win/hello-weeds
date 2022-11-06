# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 23:09:21 2022

@author: Master Zhang
"""

import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError 异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
# bugId = input("请输入bugId: ")

bugId = "109677606"

# url_aft = 'bugzilla.unisoc.com/bugzilla/show_bug.cgi?id='
url_aft = 'https://blog.csdn.net/Hexuefu_Bayonet/article/details/'

url = url_aft + bugId ;
print(url)

r = requests.get(url)
r.status_code
r.text

r.encoding
r.apparent_encoding

r.encoding = 'utf-8'

soup = BeautifulSoup(r.text,'html.parser')  # 'html.parser'这是BeautifulSoup库的HTML解析器的用法,用于解析HTML


soup.find_all('div',id="content_views",class_="markdown_views prism-atom-one-dark")

dd = soup.text.strip()
print(dd)





## 百度一下 获取标题
    
import requests
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError 异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
    
if __name__ == "__main__":
    
    url = 'https://www.baidu.com/'
    demo =getHTMLText(url)
    print(getHTMLText(url))
    
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text,'html.parser')  # 'html.parser'这是BeautifulSoup库的HTML解析器的用法,用于解析HTML
   
    
    soup.find_all('div',class_='info')
    
    # soup.text.strip()
    
    titles = soup.select('title')
    for title in titles:                  # 使用循环输出爬取到的网页上的所有新闻标题
    	print(title.text)
    
    
    

    
    
    
    
    
##  获取公司名字
import requests
from bs4 import BeautifulSoup

req = requests.get(url="https://www.crrcgo.cc/admin/crr_supplier.html?page=1")
req.encoding = "utf-8"
html=req.text
soup = BeautifulSoup(req.text,features="html.parser")
company_item = soup.find("div",class_="detail_head")
dd = company_item.text.strip()
print(dd)


   

##  豆瓣电影
from requests_html import HTMLSession
session=HTMLSession()
url=session.get('https://movie.douban.com/top250?format=text')
contents=url.html.find('#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.bd > p:nth-child(1)',first=True)
#将选择器信息作为find方法中第一个参数键入，加上first参数，值为Ture
print(contents.text)
#输出requests_html的元素的文本属性，得到目标文本(content变量类型为requests_html.Element)


##  python123
from requests_html import HTMLSession
session=HTMLSession()
url=session.get('https://python123.io/index')

str = '#links > div:nth-child(1) > div.main > div > div.index-page > section.section.is-light > div > div > div:nth-child(3) > a > div > div > div.desc'
contents=url.html.find(str,first=True)
#将选择器信息作为find方法中第一个参数键入，加上first参数，值为Ture
print(contents.text)
#输出requests_html的元素的文本属性，得到目标文本(content变量类型为requests_html.Element)




##  python123
from requests_html import HTMLSession
session=HTMLSession()
url=session.get('https://www.csdn.net/?spm=1031.2352.3001.4476')

str = 'body > div.passport-container.passport-container-mini > div > div > div.login-box > div.login-box-top > div > div.login-box-tabs-items > span.tabs-active'
contents=url.html.find(str,first=True)
#将选择器信息作为find方法中第一个参数键入，加上first参数，值为Ture
print(contents.text)



















