import socket
import threading 

port = 5050
ip = socket.gethostbyname(socket.gethostname())             #gets the IP of Host machine 
print(ip)
addr = (ip,port)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #creates a socket-> family AF_INET(IPV4) and SOCK_STREAM(TCP)
server.bind(addr)                                           #binds the socket with IP and port

def handle_client(conn,client):                             #method to handle each client on different thread
    print(f"{client} connected")                            
    connected = True
    while connected:
        msg_length = conn.recv(100).decode("utf-8")         #recieves and decode the message length (note the length<=100)
        if msg_length=="":
            continue
        elif len(msg_length)>100:
            print("message too long")
        else:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode("utf-8")     #recieves and decode the actual message 
            print(msg)
        if msg == "disconnect":                             #if message recieved is disconnect than the connection breaks
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

def start():                                                        #method that creates different thread for each client
    server.listen()                                                 #listens for the client that wants to connect
    print("Waiting for client(s) to connect...")
    while True:
        conn,client_addr=server.accept()
        client = threading.Thread(target=handle_client,args=(conn,client_addr))
        client.start()

print("Starting server...")
start()
