from zabbix_mail import mail
from datetime import datetime

receive_addr = ['13240363594@163.com', '502434432@qq.com']
files = ['work.py', 'fork.py', 'lock.py']
subject = ('%s的测试' % datetime.today().strftime('%H-%M-%S'))
mail(receive_addr, subject, files)