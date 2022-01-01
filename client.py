import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT) # convert string to bytes
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) # make length == 64 bytes 
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
input()
send("Hello SHWAN!")
input()
send("Hello Shan!")
input()
send("Hello Benson!")
input()
send(DISCONNECT_MESSAGE)