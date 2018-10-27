Secure X : Chat App 
===

### Abstract

A simple chat app which can be used to securely send encrypted texts between two or more users with the help of different python tool kits.

### Introduction

This project is based on networking using python programming language and secure communication between two or more users with the help of a simple chat app. For accomplishing this we use two python scripts , One for the server and the other for the client. The texts are encrypted with the help of a python cryptography toolkit called pycrypto.

### Workflow Diagram

## 

![alt text](https://raw.githubusercontent.com/aswinrprasad/ChatApp_PyProject/master/export%20(1).jpg)

#### Progress :

1)Designing Server side python script and debugging it.

2)Base python script for client side.

3)Giving a graphical user interface for client.py with Tkinter.

4)Debugging Client side python script.

5)End to end Encryption with AES.


Current Status :Fixing bugs in server.py

Bug : When {quit} is typed into the chat , pipe gets broken and user exit msg won't get displayed.

	Exception in thread Thread-2:
	Traceback (most recent call last):
  	File "/usr/lib/python2.7/threading.py", line 801, in __bootstrap_inner
  	  self.run()
  	File "/usr/lib/python2.7/threading.py", line 754, in run
  	  self.__target(*self.__args, **self.__kwargs)
  	File "server.py", line 51, in handle_client
  	  broadcast(msg, name+": ")
  	File "server.py", line 62, in broadcast
  	  sock.send(bytes(prefix)+do_decrypt(lenstr(msg)))
	error: [Errno 32] Broken pipe



