import psutil
import time 
def loop_to_wait (count):
    while count>0:
        count = count-1
        time.sleep(1)
        for proc in psutil.process_iter():
            try :
                pinfo = proc.as_dict(attrs=['pid','name'])
                if pinfo['name'] =='java.exe' and proc.status()!='running':
                    return True
            except psutil.NoSuchProcess:
                pass
            else :
                pass
    return False
res = loop_to_wait(10)