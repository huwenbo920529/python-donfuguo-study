# -*- coding:utf-8 -*-
import re
from docx import Document
# 需要先pip install docx, 然后pip install python-docx

doc = Document('11.docx')
text = ''.join((p.text for p in doc.paragraphs))
result = re.findall(r'(([\u4e00-\u9fa5。、！：；，]).?\2)', text)
for word in result:
    print word[0]

