# -*- encoding: utf-8 -*-
'''
@File    :   sync_sub_flows.py
@Time    :   2022年10月24日14:26:59
@Author  :   zws 
@Version :   1.0
@Contact :   zhuws@huayunsoft.com
usage: 
1. back up your source code first
2. copy your subflow.json into your project's folder, press f5 run it
3. start you ipa porject 
4. you will see your subflow has included in you project  
'''
import json 
import os 

json_ls = os.listdir('./')
def is_in_porj (to_check,proj_ls):
    for item in proj_ls:
        if item['process_path']== to_check['processInfo']['process_path']:
            return True 
    return False

proj_obj={}
with open('project.json','r',encoding='utf-8') as f:
    proj_obj = json.load(f)
    proj_ls = proj_obj['process_list']
    for item in json_ls:
        if item.endswith('json') and item not in ['globalParams.json','project.json'] :
            with open(item,'r',encoding='utf-8') as jf:
                item_obj = json.load(jf)
                if not is_in_porj(item_obj,proj_ls):
                    proj_ls.append(item_obj['processInfo'])
#写入
with open('project.json','w+',encoding='utf-8') as f:
    json.dump(proj_obj,f,ensure_ascii=False,indent=6)

with open('project.rpa','w+',encoding='utf-8') as f:
    json.dump(proj_obj,f,ensure_ascii=False,indent=6)