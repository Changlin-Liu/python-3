from email.mime.text import MIMEText
import smtplib
# MIMEText对象：正文 数据类型 编码
msg = MIMEText('hejingqi, this is python email', 'plain', 'utf-8')
msg['Subject'] = "python"
# from_addr = input('From: ')
from_addr = '13240363594@163.com'
# password = input('Password: ')
# password = '426118'
password = 'albnwhuwneurszaj'
# to_addr = input('To: ')
to_addr = '502434432@qq.com'
# smtp_server = input('SMTP server: ')
smtp_server = 'smtp.163.com'

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
