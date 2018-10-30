from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import Tkinter as tk
from Crypto.Cipher import AES

def do_encrypt(message):
    obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(message)
    return ciphertext

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ)
            msg_list.insert(tk.END, msg)
        except OSError:  # Possibly client has left the chat.
            break

def lenstr(msg):
    size=len(msg)
    if size%16 != 0:
        for i in range(size,600):
            if i%16 == 0:
                return msg
            else:
                msg=msg+" "
    else:
        return msg


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.sendto(bytes(do_encrypt(lenstr(msg))),ADDR)
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

top = tk.Tk()
top.title("SecureX Chat Room")

messages_frame = tk.Frame(top)
my_msg = tk.StringVar()  # For the messages to be sent.
my_msg.set("Type your name first.")
scrollbar = tk.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tk.Listbox(messages_frame, height=30, width=80, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tk.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tk.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = raw_input('Enter host: ')
PORT = raw_input('Enter port: ')
if not PORT:
    PORT = 5000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tk.mainloop()  # Starts GUI execution.

