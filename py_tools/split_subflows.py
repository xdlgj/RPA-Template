# -*- encoding: utf-8 -*-
'''
@File    :   split_subflows.py
@Time    :   2022年10月24日14:26:59
@Author  :   zws 
@Version :   1.0
@Contact :   zhuws@huayunsoft.com
usage: 
1. back up your source code first
2. copy your subflow.json into your project's folder, press f5 run it
3. start you ipa porject 
4. you will get subflow projs 
'''
import json 
import os 
import re
import shutil
import zipfile
# 
def is_in_porj (to_check,proj_ls):
    for item in proj_ls:
        if item['process_path']== to_check['processInfo']['process_path']:
            return True 
    return False

def zip_folder(startdir, out_file_name):
    z = zipfile.ZipFile(out_file_name, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '') 
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()

# find cw_*.json dependencies 
def get_refs(content):
    return re.findall('process_path.*?(cw_.+?\.json)',content)

#get cw_*.json dependencies subflow nodes from source proj 
def sync_subflows_node(proj_ls,item_obj):
    if not is_in_porj(item_obj,proj_ls):
                    proj_ls.append(item_obj['processInfo'])
    refs = get_refs(str(item_obj))+['主流程.json']
    return list(filter(lambda x :x['process_path'] in refs  ,proj_ls))

# generate new projs
def proj_generator():
    json_ls = os.listdir('./')
    proj_obj={}
    with open('project.json','r',encoding='utf-8') as f:
        proj_obj = json.load(f)
        proj_ls = proj_obj['process_list']
        for item in json_ls:
            if item.endswith('.json') and item not in ['globalParams.json','project.json','主流程.json'] :
                #create folder
                name = item[:-5]
                item_folder = os.path.abspath('../')+"/组件/"+ name
                new_folder = item_folder+"/"+ name
                if os.path.exists(new_folder):
                    shutil.rmtree(new_folder)
                os.makedirs(new_folder)
                #copy files
                shutil.copy(item,new_folder)
                shutil.copy('主流程.json',new_folder)
                with open(item,'r',encoding='utf-8') as jf:
                    item_obj = json.load(jf)
                    refs = get_refs(str(item_obj))
                    for r in refs :
                        if r == item: continue
                        shutil.copy(r,new_folder)
                    #generate proj objects
                    proj_obj['process_list'] = sync_subflows_node(proj_ls,item_obj)
                    proj_obj['project_info']['project_name']=item[:-5]
                    #write to project files
                    with open(new_folder+'/project.json','w+',encoding='utf-8') as f:
                        json.dump(proj_obj,f,ensure_ascii=False,indent=6)
                    with open(new_folder+'/project.rpa','w+',encoding='utf-8') as f:
                        json.dump(proj_obj,f,ensure_ascii=False,indent=6)
                zip_folder(new_folder,item_folder+"/"+name+".zip")

proj_generator()