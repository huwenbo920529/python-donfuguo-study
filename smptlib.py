# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_server = 'smtp.163.com'
mail_server_port = 25

mail_user = '1450703291@qq.com'
mail_pwd = 'aaa920529'

from_add = '1450703291@qq.com'
to_add = ['huwenbo_tjpu@163.com']

# 发送邮件形式和内容
msg = MIMEText('python mail test...', 'plain', 'utf-8')
msg['From'] = Header('msun', 'utf-8')
msg['To'] = Header('test', 'utf-8')

# 发送主题
subject = 'python smtp mail test'
msg['Subject'] = Header(subject, 'utf-8')

try:
    # smtp = smtplib.SMTP_SSL(mail_server, mail_server_port) # linux
    smtp = smtplib.SMTP_SSL()
    smtp.connect(mail_server, mail_server_port)
    smtp.login(mail_user, mail_pwd)
    print smtp
    smtp.sendmail(from_add, to_add, msg.as_string())
    smtp.quit()
    print '邮件发送成功！'
except smtplib.SMTPException:
    print 'Error:邮件发送失败！'

