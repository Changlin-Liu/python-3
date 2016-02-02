# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

# 处理地址编码
def _formate_addr(s):
    name, addr = parseaddr(s)
    # 将中文名称编码
    # formataddr/parseaddr处理二元元组[一个键值对，一个编码方式]
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '13240363594@163.com'
password = '******'
to_addr = 'perfect_0426@qq.com'
smtp_server = 'smtp.163.com'

# MIMEText对象：正文 数据类型 编码
# msg = MIMEText('hejingqi, this is python email', 'plain', 'utf-8')
msg = MIMEText('测试正文', 'plain', 'utf-8')
msg['From'] = _formate_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _formate_addr('Python管理员 <%s>' % to_addr)
msg['Subject'] = Header('中文测试', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
