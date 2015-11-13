import socket, time, threading
# 建立socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
s.bind(('127.0.0.1', 9999))
# 开启监听
s.listen(5)
print('Waiting for connecttion...')

# 创建处理数据的函数
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    # 接受客户端数据前想客户端发送的数据
    sock.send(b'Welcome!')
    while True:
        # 接受客户端数据
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        # 将数据处理完成后再返回客户端
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    # 完成一次数据交互后关闭连接
    sock.close()
    print('connection from %s:%s closed' % addr)

while True:
    # 接受一个连接
    sock, addr = s.accept()
    # 创建新线程来处理tcp连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
