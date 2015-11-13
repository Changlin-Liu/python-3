#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
# 创建一个socket{本地端口}，使用ipv4协议{AF_INET}，面向流的tcp协议{SOCK_STREAM}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn', 80))
# 发送请求
s.send(b'GET / HTTP/1.1\r\n\
    Host: www.sina.com.cn\r\n\
    Connection: close\r\n\r\n')
# 接受数据，一次接受1024字节，接受完毕为止
# 再使用字符串的join方法将列表组合起来，最后还原为接收的字节类型
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭socket
s.close()
# 把http头和网页分离【使用空行分隔符】
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open(b'D:\sina.html', 'wb') as f:
    f.write(html)