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

from_addr = '13240363594@163.com'
password = '******'
to_addr = 'perfect_0426@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEMultipart()
msg['Subject'] = Header('如何添加附件', 'utf-8').encode()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('Python管理者 <%s>' % to_addr)

msg.attach(MIMEText('学习如何添加附件', 'plain', 'utf-8'))

with open(r'D:\test.jpg', 'rb') as f:
    #设置附件的mime和文件名
    mime = MIMEBase('images', 'jpeg', filename='test.jpg')
    # 添加mime头部信息
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    # 读取附件内同
    mime.set_payload(f.read())
    # 编码
    encoders.encode_base64(mime)
    # 添加到邮件主题中
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()