

import os
os.system('"C:/Program Files/Internet Explorer/iexplore.exe" http://www.baidu.com')

  Type Name Class Name Notes 
 
  'mozilla' Mozilla('mozilla')   
 
  'firefox' Mozilla('mozilla')   
 
  'netscape' Mozilla('netscape')   
 
  'galeon' Galeon('galeon')   
 
  'epiphany' Galeon('epiphany')   
 
  'skipstone' BackgroundBrowser('skipstone')   
 
  'kfmclient' Konqueror() (1) 
 
  'konqueror' Konqueror() (1) 
 
  'kfm' Konqueror() (1) 
 
  'mosaic' BackgroundBrowser('mosaic')   
 
  'opera' Opera()   
 
  'grail' Grail()   
 
  'links' GenericBrowser('links')   
 
  'elinks' Elinks('elinks')   
 
  'lynx' GenericBrowser('lynx')   
 
  'w3m' GenericBrowser('w3m')   
 
  'windows-default' WindowsDefault (2) 
 
  'macosx' MacOSX('default') (3) 
 
  'safari' MacOSX('safari') (3) 
 
  'google-chrome' Chrome('google-chrome')   
 
  'chrome' Chrome('chrome')   
 
  'chromium' Chromium('chromium')   
 
  'chromium-browser' Chromium('chromium-browser')



import sys
 
import webbrowser

bugId = input("请输入bugId: ")

bugId = "123004048"

url_aft = 'bugzilla.unisoc.com/bugzilla/show_bug.cgi?id='

url_aft = 'https://blog.csdn.net/BAIFOL/article/details/'


url = addr_aft + bugId ;


webbrowser.open(addr)


import requests
from bs4 import BeautifulSoup

req = requests.get(url="https://blog.csdn.net/weixin_30364031/article/details/113975730")

req.encoding = "utf-8"
html=req.text
soup = BeautifulSoup(req.text,features="html.parser")

company_item = soup.find("head",class_="title")

dd = company_item.text.strip()

print(dd)



import requests
from bs4 import BeautifulSoup

page=requests.get('https://www.baidu.com/')

page.encoding = "utf-8"
soup = BeautifulSoup(page.text, 'html.parser')
soup.find_all('div')
dd = soup.text.strip()



import webbrowser   
IEPath = r'自己的浏览器地址'            #  例如我的：C:/Program Files/Internet Explorer/iexplore.exe   
webbrowser.register('IE', None, webbrowser.BackgroundBrowser(IEPath))  #这里的'IE'可以用其它任意名字，如IE11，这里将想打开的浏览器保存到'IE'  
webbrowser.get('IE').open('www.baidu.com',new=1,autoraise=True)  







from bs4 import BeautifulSoup
import requests
url = 'https://movie.douban.com/top250?format=text'
response = requests.get(url)
response.encoding=response.apparent_encoding
#因为网站使用的不是通用的utf-8格式，而是gzip，所以要让它判断解码格式
html = BeautifulSoup(response.text,'lxml')
#获取到的网页信息需要进行解析，使用lxml解析器，其实默认的解析器就是lxml，但是这里会出现警告提示，方便你对其他平台移植
content=html.select('#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)',first=True)
#将复制好的选择器信息放进select方法中，将获取到的内容作为tag形式放入一个列表中
content[0]

print(content[0].get_text())
#打印这个列表中第一个内容，就是我们要获得的信息





import requests
from bs4 import BeautifulSoup

req = requests.get(url="https://movie.douban.com/top250?format=text")
req.encoding = "utf-8"
html=req.text
soup = BeautifulSoup(req.text,features="html.parser")
company_item = soup.find_all("div",class_="other")

dd = company_item.text.strip()
print(dd)



import requests
from bs4 import BeautifulSoup

req = requests.get(url="https://www.crrcgo.cc/admin/crr_supplier.html?page=1")
req.encoding = "utf-8"
html=req.text
soup = BeautifulSoup(req.text,features="html.parser")
company_item = soup.find("div",class_="detail_head")
dd = company_item.text.strip()
print(dd)



from lxml import etree
import requests
url = 'https://python123.io/index'
response = requests.get(url)
response.encoding=response.apparent_encoding
label=etree.HTML(response.text)
#提取这个页面中所有的标签信息
content=label.xpath('#links > div:nth-child(1) > div.main > div > div.index-page > section.section.is-light > div > div > div:nth-child(2) > a > div > div > div.media.horizontal-align > div.media-content')


#提取span标签中class名为"is-text-small is-text-grey"的内容信息,并且存入一个列表中
try:
    print(content[0])
except:
    print("第{0}条数据处理失败")
    print(content[0])
#打印获得的文本信息


import urllib.request  
import re  
from bs4 import BeautifulSoup 
from distutils.filelist import findall 

page = urllib.request.urlopen('http://movie.douban.com/top250?format=text')  
contents = page.read()  
 #print(contents) 
soup = BeautifulSoup(contents,"html.parser") 
print("豆瓣电影TOP250" + " " +" 影片名              评分       评价人数     链接 ")   
for tag in soup.find_all('div', class_='info'):   
   # print tag 
    m_name = tag.find('span', class_='title').get_text()       
    m_rating_score = float(tag.find('span',class_='rating_num').get_text())         
    m_people = tag.find('div',class_="star") 
    m_span = m_people.findAll('span') 
    m_peoplecount = m_span[3].contents[0] 
    m_url=tag.find('a').get('href') 
    print( m_name+"        "  +  str(m_rating_score)   + "           " + m_peoplecount + "    " + m_url )  





## 百度一下 获取标题
import requests
from bs4 import BeautifulSoup

url = 'https://www.baidu.com/'

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
contents=url.html.find('#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)',first=True)
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








