# _*_coding:utf-8_*_
import string
import re
a = 'good 100 490.5'
print a.split()


emp_name = '.'
emp_name = re.sub('[^a-zA-Z0-9]', '', emp_name)
print emp_name, type(emp_name)
