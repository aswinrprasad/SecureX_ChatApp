from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from Crypto.Cipher import AES

clients = {}
addresses = {}
HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def lenstr(msg):
    size=len(msg)
    if size%16 != 0:
        for i in range(size,200):
            if i%16 == 0:
                return msg
            else:
                msg=msg+" "
    else:
        return msg

def do_decrypt(ciphertext):
    obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    message = obj2.decrypt(ciphertext)
    return message

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome to SecureX!"))
        client.send(bytes(" Type your name and press enter!"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    name = (do_decrypt(client.recv(BUFSIZ))).rstrip(' ')
    welcome = 'Welcome %s! To quit chat: type {quit} and send.' % name
    client.send(bytes(welcome))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg))
    clients[client] = name
    while True:
        msg = (do_decrypt(client.recv(BUFSIZ))).rstrip(' ')
        if msg != bytes("{quit}"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name))
            break

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix)+msg)

#def broadcast1(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
#    for sock in clients:
#        sock.send(bytes(prefix)+msg)

if __name__ == "__main__":
    SERVER.listen(5)  # Listens for 5 connections at max.
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()  # Starts the infinite loop.
    ACCEPT_THREAD.join()
    SERVER.close()
