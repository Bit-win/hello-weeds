# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 21:40:12 2022

@author: Master Zhang
"""

## 复制某一类型的文件到指定目录 。不包含子文件夹
import os
import shutil
 
def copy_allfiles(src,dest):
#src:原文件夹；dest:目标文件夹
  src_files = os.listdir(src)
  for file_name in src_files:
    print(file_name)
    if '.py' in file_name:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
          shutil.copy(full_file_name, dest)
            
 
copy_allfiles(r'D:\source\ap',r'D:\source\testtest')


## 复制所有文件到指定目录
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
                shutil.copyfile(file_path, dst_path)
            else:
                copy_demo(file_path, dst_path)
## 注意这里的斜杠需要修改​

src_path = 'D:/source/ap'

dst_path = 'D:/source/下行遍历​'
copy_demo(src_path,dst_path)
####################################################################################


#  复制文件夹中的所有某类型文件到指定文件。
import shutil
import os


def copy_spec_files(path):
    global num
    # （root，dirs，files）分别为：遍历的文件夹，遍历的文件夹下的所有文件夹，遍历的文件夹下的所有文件
    for root, dirs, files in os.walk(path):
        for file in files:
            # 文件后缀检测
            if file[-len(f_type):] == f_type:
                shutil.copyfile(root + '\\' + file, out_path + '\\%d.%s' % (num, f_type))
                print(root + '\\' + file + ' 复制成功-> ' + out_path + '\\%d.%s' % (num, f_type))
                num += 1
        for dir_son in dirs:
            copy_spec_files(dir_son)


if __name__ == '__main__':
    # 文件夹路径
    f_path = 'D:/source/ap'
    # 输出路径
    out_path = 'D:/source/testtest'
    # 文件类型后缀
    f_type = 'log'
    num = 1
    copy_spec_files(f_path)



























