import socket

class ChatClient():

	def __init__(self,port,host = 'localhost', kewyword = '¬'):
		self.port = port
		self.host = host
		self.kewyword = kewyword
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.host,self.port))

	def send_message()
