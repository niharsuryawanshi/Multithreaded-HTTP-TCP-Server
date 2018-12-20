#Server socket code
#Nihar Suryawanshi
#UTA id: 1001654583

import Tkinter
from socket import *
from threading import Thread
import threading
import time
import datetime
import re
from Queue import Queue

top = Tkinter.Tk()
top.title("High Power Distributed Server")
ch_sr = 1


global q
q = Queue()

#METHOD TO ACCEPT NEW INCOMMING CONNECTIONS
def accept_con():
	op_wind.insert(Tkinter.END,"Waiting for client..")
	while 1:
		#Listening to the incomming request
		connectionSocket, addr = serverSocket.accept()

		t3=Thread(target = cordintor)
		t3.daemon=True
		t3.start()
		#creating new thread for incoming client
		t2=Thread(target = listen_to_client, args = (connectionSocket,addr))
		t2.daemon = True
		t2.start()

		
#https://docs.python.org/3/library/queue.html
#Deque function is taken care here for each tread in queue.
def cordintor():
	while 1:
		time.sleep(0.5)
		e = q.get(block=True)
		e.set()

# def dispQ():
# 	while 1:
# 		time.sleep(5)
# 		op_win02.insert(Tkinter.END,str(q))



#THIS METHOD PROCESSES THE REQUEST OF CONNECTED CLIENTS, SOCKET OBJECT AND ADDRESS ARE PARAMATERS.
#https://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client
def listen_to_client(connectionSocket,addr):
	lab01=0
	op_win02.insert(Tkinter.END,"Client "+str(addr)+" Connected.")
	while ch_sr!=0:
		try:

			#receiving message from client
			message = connectionSocket.recv(2024)
			
			#Handling client disconnection.
			if message == "exit":
				op_win02.insert(Tkinter.END,"Client "+str(addr)+" Disconnected.")
		 		connectionSocket.close()
		 		lab01=1
		 		break

		 	else:
		 		op_wind.insert(Tkinter.END,"******************************************************")
		 		op_wind.insert(Tkinter.END,"REQUEST from client:" +str(addr))
		 		ms_arr = message.split('\n')
		 		#printing the HTTP request on GUI
		 		for i in ms_arr:
		 			op_wind.insert(Tkinter.END,i)
		 		
		 		#handeling mutual exclusion
		 		#https://docs.python.org/2/library/threading.html
		 		#https://www.bogotobogo.com/python/Multithread/python_multithreading_Event_Objects_between_Threads.php
		 		event = threading.Event()
		 		q.put(event)
		 		event.wait()

		 		#Server Sleep code	
				time.sleep(int(i))
				op_wind.insert(Tkinter.END,"******************************************************")

				op_wind.insert(Tkinter.END,"server slept for "+i+" seconds for client: "+str(addr))
				op_wind.insert(Tkinter.END,"******************************************************")

				#forming a HTTP Response
				now = datetime.datetime.now()
				d1="HTTP/1.1 200 OK\r\n"
				d2="Date:"+str(now)+"\r\n"
				d3="Server: Python/2.7\r\n"
				d4="Content-Type: text/html\r\n"
				d5="Content-Length: 41\r\n"
				bdy="server waited "+i+" seconds for client "+str(addr)
				data = d1+d2+d3+d4+d5+bdy

				#converting the http string into string array for display purpose
				resp_arr=data.split('\n')
				#printing HTTP response
				op_wind.insert(Tkinter.END,"RESPONSE to client: "+str(addr))
				for j in resp_arr:
					op_wind.insert(Tkinter.END,j)

				op_wind.insert(Tkinter.END,"******************************************************")

				connectionSocket.send(data)
		except Exception as ex:
			print(ex)
			break
			connectionSocket.close()
	
	if lab01!=1:
		#Code to close the server		
		op_wind.insert(Tkinter.END,"Server Shutting down..")
		connectionSocket.close()

#METHOD TO START THE SERVER
def start_server():
	#Starting new Thread to stop GUI Freeze
	op_wind.insert(Tkinter.END,"Starting the Server..")	
	t1 = Thread(target = accept_con)
	t1.daemon = True
	t1.start()
	
#METHOD TO STOP THE SERVER
def stop_server():
	global ch_sr
	ch_sr=0


#http://www.eg.bucknell.edu/~cs363/2016-spring/lecture-notes/06-SocketProgramming.pptx
#Code to define 
serverPort = 5661
#creating a socket object ServerSocket
serverSocket = socket(AF_INET, SOCK_STREAM) 
#this method binds the socket object to address host name and port no
serverSocket.bind(('',serverPort))
serverSocket.listen(3) #maximum no of Queue connection is set to 5


#https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
#Code For GUI 
btn_start = Tkinter.Button(top,text="Start", command = start_server)
btn_start.grid(row=0, column=0)

btn_close = Tkinter.Button(top,text="Stop", command = stop_server)
btn_close.grid(row=0, column=1)

Tlab1 = Tkinter.Label(top,text="Connection Status")
Tlab1.grid(row=1,columnspan=2)

op_win02 = Tkinter.Listbox(top,height=8,width=40)
op_win02.grid(row=2 ,columnspan=2)

Tlab2 = Tkinter.Label(top,text="Console")
Tlab2.grid(row=3,columnspan=2)

op_wind = Tkinter.Listbox(top,height=20, width=40)
op_wind.grid(row=4,columnspan=2)

# op_wind03 = Tkinter.Listbox(top,height=4,width=40)
# op_wind03.grid(row=5,columnspan=2)

top.mainloop()