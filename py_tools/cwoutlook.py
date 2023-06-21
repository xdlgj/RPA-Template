# -*- encoding: utf-8 -*-
'''
@File    :   cwoutlook.py
@Time    :   2022/05/29 20:41:16
@Author  :   zws 
@Version :   1.0
@Contact :   zhuws@huayunsoft.com
usage: 
1.
2.
3.
4.
'''
import win32com,os

class cwoutlook(object):
    
    def __init__(self,account_name):
        self.outlook_app = win32com.client.Dispatch("Outlook.Application")
        self.outlook = self.outlook_app.GetNamespace("MAPI")
        self.inbox = self.outlook.Folders(account_name)
        pass
        
    # 获取outlook 文件夹
    def getFloder(self,folders, name):
        for folder in folders:
            if folder.Name == name:
                return folder
            res = self.getFloder(folder.Folders, name)
            if res != None:
                return res
        return None


    # outlook 发送邮件
    def send_mail(self,to, cc, subject,content, attachment):
        if to == 'None':
            return
        mail_item = self.outlook_app.CreateItem(0)  # 0: olMailItem
        mail_item.To = to.replace(',',";")  # 收件人
        if cc != 'None':
            mail_item.CC = cc.replace(',',";")  # 抄送人
        mail_item.Subject = subject

        mail_item.BodyFormat = 2          # 2: Html format
        mail_item.HTMLBody = content
        for item in attachment:
            mail_item.Attachments.Add(item)
        mail_item.Send()


    def pull_email(self):
        self.outlook.SendAndReceive(False)  # 异步收取
        return self
        # time.sleep(120)#等待两分钟
        
    def down_attachments(self,folder,dir,move_to_dir):
        global template_path,source_path
        if len(folder.Items) == 0:
            return "no messages"
        message = folder.Items[0]

        attachments = message.Attachments
        for attachment in attachments:
            if ".xlsx" in attachment.FileName:
                attachment.SaveAsFile(os.path.join(dir, str(attachment)))
        return message

    def move_to_dir(self,message,move_to_dir):
        message.Move(self.getFloder(self.inbox.Folders, move_to_dir))