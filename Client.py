import socket

port = 5050
ip = # Here goes the IP of server. If it a local host than you can use this socket.gethostbyname(socket.gethostname()) instead of hardcoding the IP
addr=(ip,port)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addr)

def send_Message(msg):
    msg_length = len(msg)
    msg_length = str(msg_length)+f" "*(100-msg_length)
    msg_length = msg_length.encode("utf-8")
    msg = msg.encode("utf-8")
    client.send(msg_length)
    client.send(msg)
    msg_server_len = client.recv(100).decode('utf-8')
    msg_server_len = int(msg_server_len)
    msg_server = client.recv(msg_server_len).decode('utf-8')
    print(msg_server)

while True:
    msg = input()
    send_Message(msg)
    if msg=="disconnect":
        break
