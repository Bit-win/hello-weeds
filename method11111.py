# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 17:31:48 2022

@author: Master Zhang
"""

import shutil
import os
import requests
from bs4 import BeautifulSoup

# 将目录的文件复制到指定目录
def copy_demo(src_dir, dst_dir):
    """
    复制src_dir目录下的所有内容到dst_dir目录
    :param src_dir: 源文件目录
    :param dst_dir: 目标目录
    :return:
    """
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    if os.path.exists(src_dir):
        for file in os.listdir(src_dir):
            file_path = os.path.join(src_dir, file)
            dst_path = os.path.join(dst_dir, file)
            if os.path.isfile(os.path.join(src_dir, file)):
                shutil.copyfile(file_path, dst_path)
            else:
                copy_demo(file_path, dst_path)
                print("----------------存在多级文件夹，正在复制------------")

url = "https://blog.csdn.net/weixin_44791964/article/details/113682561"
kv = {'user-agent':'Mozilla/5.0'}	#浏览器身份标识
r = requests.get(url,headers=kv)
r.encoding = 'utf-8'
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
dd = soup.find_all('h2')
dd[0].text


#获取的 bug 的名字, 根据名字创建对应的文件夹
title_name = soup.title.text

print("提取到的bug的名字：" + title_name)

name = title_name

# 创建新的文件夹的基地目录
path = 'D:/source/'

# 获得创建新的文件夹所需要的名字
dst_path =os.path.join(path,name)

print("新建文件夹的名字是：""【",dst_path,"】")


if (os.path.exists(dst_path) == True):
    print("-----------------该文件夹已经存在-----------------")
else:
    os.mkdir(dst_path)
    print("------------------文件夹创建成功------------------")

#获取的资料所在的路径，并去复制粘贴
dd[3] = 'D:/source/ap'

src_path = dd[3]
copy_demo(src_path,dst_path)
print("--------------------所有文件复制完毕------------------")



####以下  是  重命名文件夹
# =============================================================================
# newname = "testtest"
# path = 'D:/source/'
# new_name = path + newname
# if (os.path.exists(dst_path) == True):
#     os.rename(dst_path,new_name)
#     print("文件夹重命名成功。")
# else:
#     print("该文件夹不存在了！")
# =============================================================================


# for i in range(len(dd)):
#     print(dd[i].text)
    
# dd = soup.text.strip('')





