import sys, datetime
# sys.path.append('/home/web/webhive/zscripts/')
from zabbix_mail import mail

TODAY = datetime.datetime.now()
# 发送邮件
receive_addr = ['13240363594@163.com', '502434432@qq.com']
subject = ('%s的结算' % TODAY.strftime('%Y-%m-%d'))
files = ['jiesuan_%s.xlsx' % TODAY.strftime('%Y-%m-%d')]
mail(receive_addr, subject, files)