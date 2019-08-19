# coding:utf-8
import pandas as pd

excel_path = 'baoxiaodan.xlsx'
d = pd.read_excel(excel_path)
print type(d)
print d