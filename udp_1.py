import socket
# udp服务端处理流程：
# 绑定端口--》接受客户端数据【含地址】--》返回客户端数据
# udp客户端处理流程：
# 向指定服务端发送数据【含地址】--》接受数据
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999')
while True:
    data, addr = s.recvfrom(1024)
    print('Recevied from %s:%s.' % addr)
    s.sendto(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'), addr)