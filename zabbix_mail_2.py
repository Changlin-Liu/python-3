#-*- coding:utf-8 -*-

import smtplib
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os


def mail(receiver, subject, abs_path_files):

    send_addr = 'zabbix@quxiu8.com'
    password = '******'

    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = send_addr
    if isinstance(abs_path_files, str):
        single_file = list()
        single_file.append(abs_path_files)
        abs_path_files = single_file
    for file in abs_path_files:
        file_name = os.path.basename(file)
        att = MIMEBase('application', 'octet-stream', filename=file)
        att.add_header('Content-disposition', 'attatchment', filename=('utf-8', '', file))
        att.set_payload(open(file, 'rb').read())
        encoders.encode_base64(att)
        msg.attach(att)

    # 发送邮件
    smtp = smtplib.SMTP('smtp.exmail.qq.com', 587)
    smtp.starttls()
    smtp.login(send_addr, password)
    smtp.sendmail(send_addr, receiver, msg.as_string())
    smtp.quit()
