# -*- encoding: utf-8 -*-
'''
@File    :   等待鼠标转圈结束.py
@Time    :   2022年10月24日14:37:55
@Author  :   zws 
@Version :   1.0
@Contact :   zhuws@huayunsoft.com
usage: 
1. 等待鼠标转圈结束
2. 
3.
4.
'''

import win32gui    
import time 
count =20
while count>0:
    count=count-1
    time.sleep(1)
    cur = win32gui.GetCursorInfo()
    if cur[1]!=65543:
        break
