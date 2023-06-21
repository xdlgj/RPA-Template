# -*- encoding: utf-8 -*-
'''
@File    :   format.py
@Time    :   2022年10月24日14:26:59
@Author  :   zws 
@Version :   1.0
@Contact :   zhuws@huayunsoft.com
usage: 
1. back up your source code first
2. press f5 run it
3. you will get ordered activities what is beginning from start node . 
4.
'''

import json 
import os 

def find_Node(nodes,id):
    for node in nodes :
        if id == node['id']:
            return node
    return None

def do_format(obj,file):
    lines = obj['graphData']['edges']
    nodes = obj['graphData']['nodes']
    start_node=None
    for line in lines :
        source_Node = find_Node(nodes,line['sourceNode'])
        target_Node = find_Node(nodes,line['targetNode'])
        source_Node['next']=target_Node
        if source_Node['ui_type'] == 'start_view' :
            start_node = source_Node
    left = 110
    top =60 
    node =start_node
    count =0 
    while True :
        count+=1
        if count%20 == 0 : 
            left += 300
            top =60
        top += 150 
        if not node : break  
        node['left']=left
        node['top']=top
        next =  node['next'] if 'next' in node else None 
        if not next : 
            break
        else :
            del node['next']
            node = next
   
    with open(file,'w+',encoding='utf-8') as f:
                json.dump(obj,f,ensure_ascii=False,indent=6)

json_ls = os.listdir('../')
for item in json_ls :
    if item.endswith('json') and item not in ['globalParams.json','project.json'] :
            item_obj={}
            with open(item,'r',encoding='utf-8') as jf:
                item_obj = json.load(jf)
            do_format(item_obj,item)

            
print('format end')