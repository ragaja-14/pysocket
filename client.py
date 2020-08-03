import socket

HEADER=64
PORT=5050
SERVER="192.168.__.__" # enter your server IP
ADDR=(SERVER,PORT)
FORMAT="utf-8"
DISCONNECT_MSG="! Disconnect"

my_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#A_INET- socket family that accepts IP address and SOCK_STREAM- TCP type sockets
my_client.connect(ADDR)
#the client socket created is trying to connect to server

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b' '*(HEADER-len(send_length))
    #padding the msg length to remaning bytes by adding bytespace i.e b' '
    my_client.send(send_length)
    my_client.send(message)
    print(my_client.recv(2048).decode(FORMAT))


send("hello Thanks for accepting connection")
input()
send("Here is the msg: HELLO WORLD:")

send(DISCONNECT_MSG)
