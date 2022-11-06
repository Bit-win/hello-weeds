# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 10:17:56 2022

@author: Master Zhang
"""

#课堂实验1
## 规范代码操作
import requests
from bs4 import BeautifulSoup

r=requests.head('http://www.baidu.com')
r.raise_for_status()
r.request.headers
r.headers
r.text

#课堂实验2    
r = requests.head('https://item.jd.com/100016931023.html')
r.headers
r.text


payload = {'key1':'value1','keys':'value2'}
r=requests.post('http://httpbin.org/post',data = payload)
print(r.text)


r=requests.post('http://httpbin.org/post',data = 'ABC')
print(r.text)



payload = {'key1':'value1','keys':'value2'}
r=requests.put('http://httpbin.org/post',data = payload)
print(r.text)



r=requests.post('http://www.baidu.com')
print(r.text)
r.encoding = r.apparent_encoding
print(r.text)




r = requests.request('GET','http://python123.io/ws', timeout = 10)
print(r.url)



kv = {'key1':'value1','key2':'value2'}
r = requests.request('GET','http://python123.io/ws',params = kv)
print(r.url)


kv = {'key1':'value1','key2':'value2'}
r = requests.request('POST','http://python123.io/ws',params = kv)
print(r.url)

kv = {'key1':'value1','key2':'value2'}
r = requests.request('POST','http://python123.io/ws',json = kv)
print(r.url)



hd = {'uer-agent':'Chrome/10'}
r = requests.request('POST','http://python123.io/ws',headers = hd)



fs = {'file': open('data.xls','rb')}
r = requests.request('POST','http://python123.io/ws',files = fs)

pxs = {'http': 'http://user:pass@10.10.10.1:1234',
       'https': 'https://10.10.10.1:4321'}

r = requests.request('GET','http://python123.io/ws', proxies = pxs)








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
    print(getHTMLText(url))
    
    demo =getHTMLText(url)
    soup = BeautifulSoup(demo,"html.parser")
    tit = soup.title
    print(tit)


#  京东案例
try:
    r = requests.get(url,timeout=30)
    r.raise_for_status()  # 如果状态不是200，引发HTTPError 异常
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")
    
kv = {'user-agent': 'Mozilla/5.0','cookie':'session-id=461-7339993-2852731; ubid-acbcn=461-9820123-9968107; i18n-prefs=CNY; session-token=EomRrKY9moVqf2uYdI2tCbldpivHBUdYwDwJqIdtgODRWixt5S7U5So48DZH1aE/3b/T3lAvYMqxjT7OF4oNmU6Z8WlvqmLkDHCbPF9EcDFr2nvX4kg89r7P91LaD48DxE99IrWrWwSnxVzzVfEpwBpYrTsM0lAp/pwaqtWl1oPzXAW8uawwtNtA8XC/Q5sW; session-id-time=2082729601l'}
r = requests.get('https://www.amazon.cn/dp/B07C8XX5H4/ref=lp_746782051_1_1',headers = kv)
r.status_code
r.encoding
r.encoding = r.apparent_encoding
r.text
soup = BeautifulSoup(r.text,"html.parser")
r.request.headers




import requests
def getHtmlText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0','cookie':'session-id=461-7339993-2852731; ubid-acbcn=461-9820123-9968107; i18n-prefs=CNY; session-token=EomRrKY9moVqf2uYdI2tCbldpivHBUdYwDwJqIdtgODRWixt5S7U5So48DZH1aE/3b/T3lAvYMqxjT7OF4oNmU6Z8WlvqmLkDHCbPF9EcDFr2nvX4kg89r7P91LaD48DxE99IrWrWwSnxVzzVfEpwBpYrTsM0lAp/pwaqtWl1oPzXAW8uawwtNtA8XC/Q5sW; session-id-time=2082729601l'}
        #当你用默认请求头去访问百度网站，只会返回一小段的内容，而用浏览器去访问，就有非常多的内容。
        # 因为服务器识别出默认的请求头不是一个正常的浏览器，所以只会返回一点。
        # 所以需要发送带header的请求
        #作用：模拟浏览器，获取和浏览器一样的内容
        r=requests.get(url,timeout=30, headers = kv)
        r.raise_for_status()#如果状态不是200，引发httperror异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '产生异常'
if __name__=="__main__":
    url="https://www.amazon.cn/dp/B07C8XX5H4/ref=lp_746782051_1_1"
    print(getHtmlText(url))


import requests
kv = {'wd':'python'}
r=requests.get('http://www.baidu.com',timeout=30, params = kv)
r.status_code
r.request.url
len(r.text)




import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.amazon.cn/dp/B07C8XX5H4/ref=lp_746782051_1_1')

r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo,"html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))
    
    
    
soup.prettify()
print(soup.prettify())


soup.p
soup.p.string
soup.p.a
soup.p.a.string


soup.title

soup.title.string
soup.title.text


tag = soup.a
tag.string
type(tag)
tag.attrs
tag.attrs['class']
type(tag.attrs)


























    

    
