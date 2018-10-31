Secure X : Chat App 
===

### Abstract

A simple chat app which can be used to securely send encrypted texts between two or more users with the help of different python tool kits.

### Introduction

This project is based on networking using python programming language and secure communication between two or more users with the help of a simple chat app. For accomplishing this we use two python scripts , One for the server and the other for the client. The texts are encrypted with the help of a python cryptography toolkit called pycrypto.

### Features

+ End-to-end encryption with AES
+ Totally Secure
+ 5 or less People Chatroom
+ GUI with Tkinter

### Requirements

+ Tkinter
	
		sudo apt-get install python-tk

+ Pycrypto

		sudo pip install pycrypto

+ Python (2.7 in my case)


### Workflow Diagram

## 

![alt text](https://raw.githubusercontent.com/aswinrprasad/ChatApp_PyProject/master/export%20(1).jpg)

#### Progress :
1)Designing Server side python script and debugging it.

2)Base python script for client side.

3)Giving a graphical user interface for client.py with Tkinter.

4)Debugging Client side python script.

5)End to end Encryption with AES.

6)Converting the code from Local Machine communication to communicate with two or more different devices.

7)Autoget IP address of server computer and store it into HOST.

#### Current Status : Bug fixing complete.
Bug 1:(fixed) When {quit} is typed into the chat , pipe gets broken and user exit msg won't get displayed.

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

#### To find your HOST value to be set : (Not needed Anymore! The IP will be fetched automatically and displayed in the latest version :D)

	$ifconfig

The result will be somewhat like this :
	
	eno1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether ec:8e:b5:53:fb:bd  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

	lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 9992  bytes 698485 (698.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 9992  bytes 698485 (698.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

	wlo1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.43.87  netmask 255.255.255.0  broadcast 192.168.43.255
        inet6 fe80::f59f:5412:fab0:a52d  prefixlen 64  scopeid 0x20<link>
        ether 30:e3:7a:0b:2b:51  txqueuelen 1000  (Ethernet)
        RX packets 68111  bytes 36842009 (36.8 MB)
        RX errors 0  dropped 3  overruns 0  frame 0
        TX packets 55794  bytes 15645620 (15.6 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

We need the address next to inet in wlo1 to be set in the HOST.


#### For further Development Fork and commit changes. 
