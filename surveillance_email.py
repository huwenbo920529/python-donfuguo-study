# -*- coding:utf-8 -*-
import time
import datetime
from poplib import POP3_SSL
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


pop_server_address = 'pop.163.com'
# email_address = input('please input email address:')
# pwd = input('please input password:')
email_address = "huwenbo_tjpu@163.com"
pwd = "a920529"

last_num = 1
# while True:
#     server = POP3_SSL(pop_server_address)  # 建立连接
#     server.set_debuglevel(0)  # 不显示与服务器之间的交互信息
#     server.user(email_address)  # 登陆
#     server.pass_(pwd)
#     _, mails, _ = server.list()  # 获取全部邮件的编号，mails的格式为['mesg_num octets', ...]
#     print server.list()
#     server.quit()  # 退出
#     newest_number = int(mails[-1].split()[0])
#     if newest_number != last_num:
#         print '{}--您有{}封未读的邮件'.format(str(datetime.datetime.now())[:19], newest_number-last_num)
#         last_num = newest_number
#     time.sleep(60)

server = POP3_SSL(pop_server_address)  # 建立连接
server.set_debuglevel(1)  # 显示与服务器之间的交互信息
server.user(email_address)  # 登陆
server.pass_(pwd)
_, mails, _ = server.list()  # 获取全部邮件的编号，mails的格式为['mesg_num octets', ...]
mail_nums = list(map(lambda item: int(item.split()[0]), reversed(mails)))[:100]  # 获取最新的100封邮件的编号

fp = open('date.txt', 'w')  # 用来存储邮件日期的文件
for num in mail_nums:
    try:
        _, lines, _ = server.retr(num)  # lines是一个字节串列表，存放了改邮件的所有行
    except:
        continue

    for line in lines:
        line = line.strip()
        if line.startswith(b'Date:'):
            receive_time = line.decode()[5:]
            print receive_time
            break
    else:
        continue

    # 适当修正不合适的日期时间格式
    dt = receive_time[:30].split()
    if len(dt) < 5:
        continue
    if len(dt[3]) == 2:
        dt[3] = '20' + dt[3]
    receive_time = ' '.join(dt)
    try:
        receive_time = time.strptime(receive_time[0:receive_time.rindex(':')+3].strip(), "%a, %d %b %Y %H:%M:%S")
    except:
        receive_time = time.strptime(receive_time[0:receive_time.rindex(':')+3].strip(), "%d %b %Y %H:%M:%S")
    receive_time = time.strftime('%Y-%m-%d %H:%M:%S', receive_time)
    # 只关心年份和月份
    ymd = receive_time[:7]
    print ymd
    fp.write(ymd+'\n')
fp.close()
server.quit()


# 读取获取的时间数据
with open('date.txt') as fp:
    date_frequency = fp.read().split()

# 绘制折线图
df = pd.DataFrame({'年月': date_frequency, '数量':[1]*len(date_frequency)})
df = df.groupby('年月', as_index=False).sum()

df.plot(x='年月', kind='bar')
plt.legend()
plt.show()