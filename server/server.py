from socket import  AF_INET, socket, SOCK_STREAM
from threading import Thread 
import time
from person import Person

#GLOBAL CONSTANTS
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10
BUFSIZ = 1024

#GLOBAL VARIABLES
persons = []
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR) #set up server


def broadcast(msg, name):
	"""
	send new messages to all clients
	:param msg: bytes["utf8"]
	:param name: str
	:return:
	"""
	for person in persons:
		client = person.client
		client.send(bytes(name, "utf8") + msg)



def client_communication(person):
	"""
	Thread to handle all the messages from client
	:param person: Person
	:return: None
	"""
	client = preson.client
	
	#get person name
	name = client.recv(BUFSIZ).decode("utf8")
	person.set_name(name)
	msg = bytes(f"{name} has joined the chat!", "utf8")
	broadcast(msg,"") #broadcast welcome message

	while True:	#wait from any message from person
		try:
			msg = client.recv(BUFSIZ)
			
			if msg == bytes("{quit}","utf8"):
				
				client.close()
				persons.remove(person)
				broadcast(bytes(f"{name} has left the chat.."),"")
				
				print(f"[DISCONNECTED] {name} disconnected")	
				break
			else:
				broadcast(msg,name+": ")
				print(f"{name}:",msg.decode("utf8"))
		except Exception as e:
			print("[EXCEPTION]",e)
			break



def wait_for_connection():
	"""
	Sets up handling for incoming clients
	wait for connection with new client, start new thread once connected
	:param SERVER: SOCKET
	:return: None
	"""
	
	while True: 
		try:
			clients, addr = SERVER.accept()#wait for any new connections
			person = Person(addr, name, client)
			persons.append(person)
			print(f"[CONNECTION] {addr} conneted to the server at {time.time()}")
			Thread(target = clients_communication, args = (person,)).start()
		except Exception as e:
			print("[EXCEPTION]",e)
			
	print("SERVER CRASHED")


if __name__ == "__main__":
	SERVER.listen(MAX_CONNECTIONS) #listening for connection
	print("[STARTED] waiting for connection...")
	ACCEPT_THREAD = Thread(target = wait_for_connection)
	ACCEPT_THREAD.start()
	ACCEPT_THREAD.join()
	SERVER.close()

