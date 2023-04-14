import socket
import threading

# 创建一个TCP套接字并绑定到本地地址
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 12345))

# 等待客户端连接并创建新线程进行处理
def handle_client(conn, addr):
    while True:
        try:
            # 接收客户端消息并广播到所有客户端
            message = conn.recv(1024).decode('utf-8')
            if message:
                print(f"{addr[0]}:{addr[1]}: {message}")
                broadcast_message(message, conn)
            else:
                # 客户端已经关闭连接
                break
        except:
            # 出现错误
            break

    # 关闭套接字连接
    conn.close()

# 广播消息给所有客户端
def broadcast_message(message, sender_conn):
    for conn in connections:
        if conn != sender_conn:
            conn.send(message.encode('utf-8'))

# 监听客户端连接请求并创建新线程进行处理
connections = []
while True:
    s.listen()
    conn, addr = s.accept()
    connections.append(conn)
    print(f"New client connected: {addr[0]}:{addr[1]}")
    threading.Thread(target=handle_client, args=(conn, addr)).start()
