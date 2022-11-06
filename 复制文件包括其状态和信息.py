# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 11:04:06 2022

@author: Master Zhang
"""

import shutil
import os


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
                shutil.copy2(file_path, dst_path)
            else:
                copy_demo(file_path, dst_path)
                print("存在多级文件夹，正在复制。")
                
#源文件路径
source_path = r'D:\source'
#目标路径
target_path  = r'D:\target' 

copy_demo(source_path,target_path)

# filename是文件的名字+后缀名;

# from_path 就是当前这个被遍历出来的文件的完整路径;

# to_path是这个文件要复制到的路径。

# shutil 的 copy() 是复制到一个新的地方，创建时间、修改时间、访问时间都是新的;

# copy2() 则是会创建时间、修改时间、访问时间这些也复制过去。