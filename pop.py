# -*- encoding:utf-8 -*-
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

email = '13240363594@163.com'
password = '******'
pop3_server = 'pop.163.com'

# 获取邮件编码方式
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

# 对邮件地址/subject的名字处理
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value
# 
def print_info(msg, indent=0):
    # 处理邮件头部
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    # 递归打印message对象
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s----------' % ('  ' * indent))
            print_info(part, indent + 1)
    # 如果已经是基础对象[文本、图像、附件]则处理数据
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

# 登陆服务器
server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))
server.user(email)
server.pass_(password)

# 显示邮件的数量和占用空间
print('Count: %s Size: %s' % server.stat())
# 返回消息的编号
res, mails, octets = server.list()
print(mails)
# 建立索引返回最新的邮件每一行内容
index = len(mails)
res, lines, octets = server.retr(index)
# 将邮件的行拼接成完整邮件
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 将邮件内容转换为可处理的message类型
msg = Parser().parsestr(msg_content)
print_info(msg)
server.quit()
