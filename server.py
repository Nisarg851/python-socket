import socket
import threading 

port = 5050
ip = socket.gethostbyname(socket.gethostname())
print(ip)
addr = (ip,port)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addr)

def handle_client(conn,client):
    print(f"{client} connected")
    connected = True
    while connected:
        msg_length = conn.recv(100).decode("utf-8")
        if msg_length=="":
            continue
        elif len(msg_length)>100:
            print("message too long")
        else:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode("utf-8")
            print(msg)
        if msg == "disconnect":
            connected = False
            print(f"{client} disconnected")
        msg_client = input()
        msg_client_length = len(msg_client)
        msg_client_length = str(msg_client_length) + f" "*(100-msg_client_length)
        msg_client_length = msg_client_length.encode('utf-8')
        msg_client = msg_client.encode('utf-8')
        conn.send(msg_client_length)
        conn.send(msg_client)
        
    conn.close()

def start():
    server.listen()
    print("Waiting for client(s) to connect...")
    while True:
        conn,client_addr=server.accept()
        client = threading.Thread(target=handle_client,args=(conn,client_addr))
        client.start()

print("Starting server...")
start()