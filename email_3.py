# -*- coding:utf-8 -*-
# 构建文件文本结构
from email.mime.text import MIMEText
# 构建文件非文本结构
from email.mime.base import MIMEBase
# 构建邮件主体
from email.mime.multipart import MIMEMultipart
# 处理邮件头部
from email.header import Header
# 处理邮件地址
from email.utils import parseaddr, formataddr
# 处理邮件编码
from email import encoders
# 负责邮件发送
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
"""
from_addr = '13240363594@163.com'
password = '******'
to_addr = '502434432@qq.com'
smtp_server = 'smtp.163.com'
smtp_port = 25
"""
from_addr = 'zabbix@admin.com'
password = '******'
to_addr = '502434432@qq.com'
smtp_server = 'smtp.exmail.qq.com'
smtp_port = 587

msg = MIMEMultipart()
msg['Subject'] = Header('正文显示图片', 'utf-8').encode()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('Python管理者 <%s>' % to_addr)

msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"</p>' +
    '</body></html>', 'html', 'utf-8'))

with open(r'D:\test.jpg', 'rb') as f:
    #设置附件的mime[即content-type等信息]
    mime = MIMEBase('images', 'jpeg', filename='thumb.jpg')
    # 添加mime头部信息
    mime.add_header('Content-Disposition', 'attachment', filename='thumb.jpg')
    # 设置附件的id，用于html嵌入的调用
    mime.add_header('Content-ID', '0')
    # 读取附件内内容
    mime.set_payload(f.read())
    # 编码
    encoders.encode_base64(mime)
    # 添加到邮件主题中
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, smtp_port)
# server.connect(smtp_server, smtp_port)
server.starttls()
# server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()