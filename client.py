import socket, time
"""
客户端处理流程：
建立连接--》发送数据--》接受数据--》关闭连接
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
# 告诉服务器结束连接
s.send(b'exit')
s.close()