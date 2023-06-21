# -*- encoding: utf-8 -*-
'''
@File    :   cwpfile.py
@Time    :   2022/05/27 16:00:35
@Author  :   zws 
@Version :   1.0
@Contact :   zhuws@huayunsoft.com
usage: 
1.
2.
3.
4.
'''

import pandas as pd
import openpyxl as xl
from itertools import islice


#### 参数###

# p_file = r"C:\Users\zws\Desktop\总账一般账户余额结平.2.0.92\lib\net45\参数文件\paramsFile.xlsx"

# sheet_name = "参数表"

### 参数 ##
_g = globals()


def getStr(v):
    return str(v) if v else ""


def read_excel(filename=None, sheet_name=None, wb=None):
    if wb == None:
        wb = xl.load_workbook(filename)
    col_first = 0
    ws = wb[sheet_name] if sheet_name != None else wb.active
    data = ws.values
    cols = next(data)[col_first:]
    data = list(data)
    data = (islice(r, col_first, None) for r in data)
    df = pd.DataFrame(data, columns=cols)
    df.columns = df.columns.astype(str)
    wb.close()
    return df


def read_params():
    global sheet_name, p_file, ps, df, error_msg
    error_msg = ""
    df = read_excel(filename=p_file, sheet_name=sheet_name if sheet_name !=
                    None else "参数表").dropna(how='all').fillna('').astype(str)
    ps = {}
    for key in list(df.values):
        name = key[0]
        value = key[1]
        try:
            ps[name] = value
            _g[name] = getStr(value)
        except Exception as ex:
            error_msg += ex
            pass


read_params()
