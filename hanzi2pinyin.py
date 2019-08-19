# -*- coding:utf-8 -*-
from pypinyin import lazy_pinyin, pinyin

a = lazy_pinyin(u'这是一个汉字转拼音的python测试例子') #返回拼音
print '不带声调:',
for i in a:
    print i,
print '\n'

b = lazy_pinyin(u'这是一个汉字转拼音的python测试例子', 1) #带声调的拼音
print '带声调:',
for i in b:
    print i,
print '\n'

c = lazy_pinyin(u'这是一个汉字转拼音的python测试例子', 2) #带声调的拼音,另一种风格
print '带声调:',
for i in c:
    print i,
print '\n'

d = lazy_pinyin(u'这是一个汉字转拼音的python测试例子', 3) #只返回拼音首字母
print '只返回拼音首字母:',
for i in d:
    print i,
print '\n'

e = pinyin(u'重阳')  # 返回拼音
print '带声调:',
for i in e:
    for j in i:
        print j,
print '\n'

f = pinyin(u'重阳节', heteronym=True)  # 返回多音字的所有读音
print '带声调多音字:',
for i in f:
    for j in i:
        print j,
print '\n'

import string
def strip_substring(strsrc, substrings):
    """ strip the substrings from the string
    :param strsrc:
    :param substrings:
    :return: strsrc
    """
    for substring in substrings:
        strsrc = string.replace(strsrc, substring, '')
    return strsrc

home_phone = ''
substrings = ('(', ')', '-', '_')
home_phone = strip_substring(home_phone, substrings)
print 'home_phone', home_phone, type(home_phone)
