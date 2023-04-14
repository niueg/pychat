from tkinter import *
import socket
import threading

# 初始化GUI窗口
root = Tk()
root.title("Chat Room")

# 创建一个TCP套接字并连接到服务器
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 12345))

# GUI回调函数，处理发送消息事件
def send_message():
    message = message_entry.get()
    if message:
        # 发送消息到服务器
        s.send(message.encode('utf-8'))

# GUI回调函数，处理接收消息事件
def receive_message():
    while True:
        try:
            message = s.recv(1024).decode('utf-8')
            message_listbox.insert(END, message)
        except:
            break

# 启动线程以便在后台接收消息
threading.Thread(target=receive_message).start()

# 创建GUI控件
message_label = Label(root, text="Message:")
message_label.pack(side=LEFT)

message_entry = Entry(root)
message_entry.pack(side=LEFT)

send_button = Button(root, text="Send", command=send_message)
send_button.pack(side=LEFT)

message_listbox = Listbox(root)
message_listbox.pack(side=BOTTOM)

# 运行GUI主循环
root.mainloop()

# 关闭套接字连接
s.close()
