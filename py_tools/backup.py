# -*- encoding: utf-8 -*-
'''
@File    :   backup.py
@Time    :   2022年10月24日14:37:55
@Author  :   zws 
@Version :   1.0
@Contact :   zhuws@huayunsoft.com
usage: 
1. press f5
2. you will get you source code backup 
3.
4.
'''

import os
import shutil
import time 
backup = '../../backup'
if not os.path.exists(backup):
    # 如果目标路径不存在原文件夹的话就创建
    os.makedirs(backup)
else :
    os.rename(backup,backup+time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))

shutil.copytree('../', backup,ignore= shutil.ignore_patterns('*.py'))
print('backup dir finished!')