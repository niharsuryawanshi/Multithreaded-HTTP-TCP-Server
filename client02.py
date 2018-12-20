#Client socket code
#Nihar Suryawanshi
#UTA id: 1001654583

import Tkinter
from socket import *
import time
import random
from threading import Thread
import datetime
import re

#Global Variables
top = Tkinter.Tk()
top.title("Client Handler")
serverName = 'localhost'
serverPort = 5661
ch01 = 1
ch02 = 1
ch03 = 1


#METHOD TO START CLIENT
def st():
	op_wind.insert(Tkinter.END,"Starting the client..")	
	t1 = Thread(target = start_client)
	t1.daemon = True
	t1.start()


#METHOD TO START THE CLIENT 01
def start_client01():
	#To restart the server
	global ch01
	ch01 = 1
	#http://www.eg.bucknell.edu/~cs363/2016-spring/lecture-notes/06-SocketProgramming.pptx
	clientSocket = socket(AF_INET, SOCK_STREAM)
	#connect the socket to welcoming socket
	clientSocket.connect((serverName,serverPort))	

	#starting new thread for processing input and output
	t3 = Thread(target = send_rec01,args=(clientSocket,))
	t3.deamon=True
	t3.start()

#METHOD TO START THE CLIENT 01
def start_client02():
	global ch02
	ch02 = 1
	#http://www.eg.bucknell.edu/~cs363/2016-spring/lecture-notes/06-SocketProgramming.pptx
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName,serverPort))
	#starting new thread for processing input and output
	t4= Thread(target= send_rec02,args=(clientSocket,))
	t4.deamon=True
	t4.start()

#METHOD TO START THE CLIENT 01
def start_client03():
	global ch03
	ch03 = 1
	#http://www.eg.bucknell.edu/~cs363/2016-spring/lecture-notes/06-SocketProgramming.pptx
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName,serverPort))
	#starting new thread for processing input and output
	t5= Thread(target= send_rec03,args=(clientSocket,))
	t5.deamon=True
	t5.start()


#METHOD TO SEND AND RECEIVE DATA TO AND FROM SERVER		
def send_rec01(clientSocket):
	close_fg = 0
	while ch01!=0:
		#Generating random integer
		no = random.randint(3,10)
		now = datetime.datetime.now()

		#creating HTTP request
		h1="POST / HTTP/1.1\r\n"
		h6="Host: localhost:"+str(serverPort)+"\r\n"
		h2="User-Agent: python/2.7\r\n"
		h3="Content-Type: text/html\r\n"
		h4="Content-Length: 1\r\n"
		h5="Date:"+ str(now)+"\r\n"
		b1=str(no)

		data=h1+h6+h2+h3+h4+h5+b1


		try:
			#http://www.eg.bucknell.edu/~cs363/2016-spring/lecture-notes/06-SocketProgramming.pptx
			
			#https://www.tutorialspoint.com/python/time_time.htm
			start = time.time()
			#sending http request to server
			clientSocket.sendto(data,(serverName,serverPort))
			#receiving the response from the server
			modifiedMsg, serverAddress = clientSocket.recvfrom(2024)
			end = time.time()
			waited = end-start

			#printig on GUI
			op_wind.insert(Tkinter.END,"Client 01:")
			mess_array = modifiedMsg.split("\n")
			op_wind.insert(Tkinter.END,mess_array[5])
			op_wind.insert(Tkinter.END,"Total time Client Waited : " + str(waited) + "seconds")


		except Exception as e:
			#Server closing event handeling
			close_fg = 1
			op_wind.insert(Tkinter.END,"Sumthing happened!!!Server has shut down...please try again later")
			
			print(e)
			clientSocket.close()
			break

	#client closing event handeling
	if close_fg != 1:		
		clientSocket.sendto("exit",(serverName,serverPort))
		op_wind.insert(Tkinter.END,"Client 01 Stopped..")
		clientSocket.close()

#METHOD TO SEND AND RECEIVE DATA TO AND FROM SERVER	
def send_rec02(clientSocket02):
	close_fg = 0
	while ch02!=0:
		#Generating random integer
		no = random.randint(3,10)
		now = datetime.datetime.now()

		#creating HTTP request
		h1="POST / HTTP/1.1\r\n"
		h6="Host: localhost:"+str(serverPort)+"\r\n"
		h2="User-Agent: python/2.7\r\n"
		h3="Content-Type: text/html\r\n"
		h4="Content-Length: 1\r\n"
		h5="Date:"+ str(now)+"\r\n"
		b1=str(no)

		data=h1+h6+h2+h3+h4+h5+b1


		try:
			#http://www.eg.bucknell.edu/~cs363/2016-spring/lecture-notes/06-SocketProgramming.pptx
			
			#https://www.tutorialspoint.com/python/time_time.htm
			start = time.time()
			#sending http request to server
			clientSocket02.sendto(data,(serverName,serverPort))
			#receiving the response from the server
			modifiedMsg, serverAddress = clientSocket02.recvfrom(2024)
			end = time.time()
			waited = end-start

			#printig on GUI
			op_wind.insert(Tkinter.END,"Client 02:")
			#print(modifiedMsg)
			mess_array = modifiedMsg.split("\n")
			op_wind.insert(Tkinter.END,mess_array[5])
			op_wind.insert(Tkinter.END,"Total time Client Waited : " + str(waited) + "seconds")


		except Exception as e:
			#Server closing event handeling
			close_fg = 1
			op_wind.insert(Tkinter.END,"Sumthing happened!!!Server has shut down...please try again later")
			print(e)
			clientSocket02.close()
			break

	#client closing event handeling
	if close_fg != 1:		
		clientSocket02.sendto("exit",(serverName,serverPort))
		op_wind.insert(Tkinter.END,"Client 02 Stopped..")
		clientSocket02.close()


#METHOD TO SEND AND RECEIVE DATA TO AND FROM SERVER	
def send_rec03(clientSocket03):
	close_fg=0
	while ch03!=0:

		no = random.randint(3,10)
		now = datetime.datetime.now()

		#creating HTTP request
		h1="POST / HTTP/1.1\r\n"
		h6="Host: localhost:"+str(serverPort)+"\r\n"
		h2="User-Agent: python/2.7\r\n"
		h3="Content-Type: text/html\r\n"
		h4="Content-Length: 1\r\n"
		h5="Date:"+ str(now)+"\r\n"
		b1=str(no)

		data=h1+h6+h2+h3+h4+h5+b1

		try:
			#http://www.eg.bucknell.edu/~cs363/2016-spring/lecture-notes/06-SocketProgramming.pptx
			
			#https://www.tutorialspoint.com/python/time_time.htm
			start = time.time()
			#sending http request to server
			clientSocket03.sendto(data,(serverName,serverPort))
			#receiving the response from the server
			modifiedMsg, serverAddress = clientSocket03.recvfrom(2024)
			end = time.time()
			waited = end-start

			#printig on GUI
			op_wind.insert(Tkinter.END,"Client 03:")
			mess_array = modifiedMsg.split("\n")
			op_wind.insert(Tkinter.END,mess_array[5])
			op_wind.insert(Tkinter.END,"Total time Client Waited : " + str(waited) + "seconds")

			
		except Exception as e:
			#Server closing event handeling
			close_fg = 1
			op_wind.insert(Tkinter.END,"Sumthing happened!!!Server has shut down...please try again later")
			print(e)
			clientSocket02.close()
			break

	if close_fg!=1:
		clientSocket03.sendto("exit",(serverName,serverPort))
		op_wind.insert(Tkinter.END,"Client 03 Stopped..")
		clientSocket03.close()	


#METHOD TO STOP THE CLIENT
def stop_client01():
	global ch01
	ch01=0

def stop_client02():
	global ch02
	ch02=0

def stop_client03():
	global ch03
	ch03=0


#Code For GUI 
btn_start = Tkinter.Button(top,text="Start 1", command = start_client01)
btn_start.grid(row = 0, column =0)

btn_close01 = Tkinter.Button(top,text="Stop01", command = stop_client01)
btn_close01.grid(row = 1, column =0)

btn_start02 = Tkinter.Button(top,text="Start 2", command = start_client02)
btn_start02.grid(row = 0, column =1)

btn_close02 = Tkinter.Button(top,text="Stop02", command = stop_client02)
btn_close02.grid(row = 1, column =1)


btn_start03 = Tkinter.Button(top,text="Start 3", command = start_client03)
btn_start03.grid(row = 0, column =2)

btn_close03 = Tkinter.Button(top,text="Stop03", command = stop_client03)
btn_close03.grid(row = 1, column =2)



op_wind = Tkinter.Listbox(top,height=20, width=50)
op_wind.grid(row=2,columnspan=3)

top.mainloop()