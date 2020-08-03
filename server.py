import socket
import threading

HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
DISCONNECT_MSG="! Disconnect"
FORMAT='utf-8' #used to get and send msgs in format specified
#socket.gethostname()-gives hostname of current sytem running
my_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#A_INET- socket family that accepts IP address and SOCK_STREAM- TCP type sockets
my_server.bind(ADDR)

def handle_client(conn,addr):
    print("[NEW CONNECTION] connected at {0} ",addr)
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg== DISCONNECT_MSG:
                connected=False
            print("Recieved Message:{0} \nfrom Address:{1}",msg,addr)
            conn.send("Message recieved".encode(FORMAT))

    conn.close()




def start_server():
    my_server.listen()
    #listens requests from client on the socket created at 5050 port
    print("[LISTENING] Server is litening on {0} and PORT:{1}",SERVER,PORT)
    while True:
        conn, addr=my_server.accept()
        #conn is socket object/instance created btw the client and our sever to communiciate
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        #foreach new connection new threads is created to ensure independent handling of clients
        thread.start()
        print("[ACTIVE CONNECTIONS] Currently active connections: {0}",threading.activeCount()-1)


print("[STARTING] Server is starting.... ")
start_server()