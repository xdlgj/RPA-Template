p = '导出表单.cmml'
from xml.dom import minidom


def visit(node,f,p_node):
    new_node = f(node)
    p_node['childs'].append(new_node)
    if(len(node.childNodes)!=0):
        for item in node.childNodes:
            visit(item,f,new_node)
   
def name_node(name):
    if 'Variable' == name : return '变量'
    if name =='Flowchart': return '流程图'
    if name =='FlowStep.Next': return '下一步'
    if name =='FlowStep': return '流程步骤'
    if name =='Delay': return '延时'
    if name =='If.Else': return '或'
    if name =='cmipa:Break': return '中断'
    if name =='cmipa:ClickActivity': return '单击'
    if name =='Sequence': return '序列'
    if name =='cmipa:ForEach': return '遍历'
    if name =='cmipa:ForEach.Body': return '遍历内容'
    if name =='Flowchart.StartNode': return '流程图开始节点'
    if name =='cmipa:InvokeWorkflowFileActivity.Arguments': return '子流程参数'
    if name =='cmipa:InvokeWorkflowFileActivity': return '执行子流程'
    if name =='cmipa:InvokePythonFileActivity.SysPathAppendList': return '执行python文件'
    if name =='cmipa:InvokePythonFileActivity.Arguments': return 'python文件参数'
    if name in ['#text','x:Reference','sads:DebugSymbol.Symbol'] : return 'ignore'
    return name

doc = minidom.parse(p)
ref_node = doc.getElementsByTagName("TextExpression.ReferencesForImplementation")
start_node = ref_node[0].nextSibling.nextSibling

def sample_nodes(node):
    name = name_node(node.nodeName)
    if name !='ignore' : print(name)
    return {"name":name,"childs":[]}
    
    
new_start_node ={"name":"开始","childs":[]}
visit(start_node,sample_nodes,new_start_node)


def prune(node):
    for item in node['childs']:
        prune(item)
    new_childs = []
    for item in node['childs']:
        if not ( item['name'] =='ignore' and len(item['childs'])==0):
            new_childs.append(item)
    node['childs'] = new_childs
prune(new_start_node)
print(new_start_node)

