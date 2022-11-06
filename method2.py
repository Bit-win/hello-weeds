# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 17:31:48 2022

@author: Master Zhang
"""

import shutil
import os
from requests_html import HTMLSession

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
                print("存在多级文件夹，正在复制。")



###第一种方法获取  bubbling的  文字

session=HTMLSession()
url=session.get('https://mc-july.cn/2020/10/30/python-c-4/')

str_tit = '#post > article > section > div.post-content.markdown-body > p:nth-child(49) > strong'
contents_tit=url.html.find(str_tit,first=True)
#将选择器信息作为find方法中第一个参数键入，加上first参数，值为Ture
str_content = '#标签树的下行遍历 > strong'
contents_cont=url.html.find(str_content,first=True)


#获取的 bug 的名字, 根据名字创建对应的文件夹
title_name = contents_tit.text

print("bug的名字：" + title_name)

name = title_name

# 创建新的文件夹的基地目录
path = 'D:/source/'

# 获得创建新的文件夹所需要的名字
dst_path =os.path.join(path,name)

if (os.path.exists(dst_path) == True):
    print("该文件夹已经存在！")
else:
    os.mkdir(dst_path)
    print("文件夹创建成功！")

#获取的资料所在的路径，并去复制粘贴
contents_cont._text = 'D:/source/ap'

src_path = contents_cont._text
copy_demo(src_path,dst_path)




