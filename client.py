import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),7888))
msg = s.recv(1024)
print(msg.decode())
