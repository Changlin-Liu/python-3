#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr
import os

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

sender = 'zabbix@admin.com'
password = '******'
receiver = 'perfect_0426@qq.com'

# 添加邮件格式
msg = MIMEMultipart('alternative')
msg['Subject'] = Header('中文附件', 'utf-8')
msg['From'] = _format_addr('监控账号 <%s>' % sender)
msg['To'] = _format_addr('何静奇 <%s>' % receiver)

# 添加html信息
html = """
<html>
    <body>
    测试页面
    <a href="http://www.admin.com">ceshi</a>
    <p><img src="cid:images1"></p>
    </body>
</html>
"""
htm = MIMEText(html, 'html', 'utf-8')
msg.attach(htm)

# 添加图片
fp = open(r'D:\thumb.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<images1>')
msg.attach(msgImage)

# 添加附件
file = r'D:\设备登记.xlsx'
name = os.path.basename(file)
att = MIMEText(open(name, 'rb').read(), 'base64', 'utf-8')
att.add_header('Content-Type',\
 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
att.add_header('Content-disposition', 'attatchment', filename=('gb2312', '', name))
msg.attach(att)

# 发送邮件
smtp = smtplib.SMTP('smtp.exmail.qq.com', 587)
smtp.set_debuglevel(1)
smtp.starttls()
smtp.login(sender, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
