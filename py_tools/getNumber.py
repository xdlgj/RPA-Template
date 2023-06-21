import os
import time 
wait_file_path = 'C:\\Users\\zws\\Desktop\\4.xls'
count =10
res =False
while count>0 :
    count = count -1 
    if os.path.exists(wait_file_path):
        res =True
        break;
    else :
        time.sleep(1)