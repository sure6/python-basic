# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年06月19日
"""
import os
import shutil

print(os.getcwd())

# if os.path.exists('data_write.txt'):
#     os.remove('data_write.txt')


# dirpath = r'd:\dirdemo\subdir'
# if not os.path.exists(dirpath):
#     # os.mkdir(dirpath)
#     os.makedirs(dirpath)
# else:
#     # os.rmdir(dirpath)
#     shutil.rmtree(dirpath)



# filenames = os.listdir(os.getcwd())
# for fname in filenames:
#     print(fname)

# for files in os.walk(os.getcwd()):
#     print(files)

# 序列解包
for dirpath, subdirs, files in os.walk(os.getcwd()):
    for name in subdirs:
        print("目录", os.path.join(dirpath, name))
    for name in files:
        print("文件", os.path.join(dirpath, name))

