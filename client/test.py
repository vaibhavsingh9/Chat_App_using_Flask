# from socket import  AF_INET, socket, SOCK_STREAM
# from threading import Thread
# import time

# #Golabl constants
# HOST = "localhost"
# PORT = 5500
# ADDR = (HOST, PORT)
# BUFSIZ = 512

# #Golbal variables
# messages = []
# client_socket = socket(AF_INET, SOCK_STREAM)
# client_socket.connect(ADDR)

# def receive_messages():
# 	"""
# 	recv messaegs to server
# 	return none
# 	"""
# 	while True:
# 		try:
# 			msg= client_socket.recv(BUFSIZ).decode()
# 			messages.append(msg)
# 			print(msg)
# 		except Exception as e:
# 			print("[EXCEPTION]",e)
# 			break

# def send_message(msg):
# 	"""
# 	send messages to server
# 	param msg: str
# 	return None
# 	"""

# 	client_socket.send(bytes(msg,"utf8"))
# 	if msg == "{quit}":
# 		client_socket.close()

# receive_thread = Thread(target = receive_messages)
# receive_thread.start()

# send_message("Vaibhav")
# time.sleep(10)
# send_message("hello")
# time.sleep(2)
# send_message("{quit}")

# from client import Client
# c1 = Client("Tim")
# c2 = Client("Joe")

# c1.send_message("hello")
# c2.send_message("whats up")
# time.sleep(1)
# c1.send_message("nothing much, hbu")
# time.sleep(1)
# c2.send_message("Boring...")

from client import Client
import time
from threading import Thread

c1 = Client("tim")
c2 = Client("name")

def update_messages():
	"""
	update local new message
	"""
	msgs = []
	reun = True
	while run:
		time.sleep(0.1)#update every 1/10 of the second
		new_messages = c1.get_messages()#get any new messages from client
		msgs.extend(new_messages)#add to local list of mesages
		
		for msg in new_messages:#display new messages
			print(msg)

			if msg == "{quit}":
				run = False
				break

Thread(target = update_messages).start()

c1.send_message("hello")
time.sleep(5)
c2.send_message("hello")
time.sleep(5)
c1.send_message("whats up")
time.sleep(5)
c2.send_message("nothing much")
time.sleep(5)

c1.diconnect()
time.sleep(2)
c2.disconnect()