import socket

class ChatClient():

	def __init__(self,port,host = 'localhost', keyword = '¬'):
		self.port = port
		self.host = host
		self.keyword = keyword
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.host,self.port))

	def send_message(self,msg):
		if(msg == self.keyword):
			self.s.close()
			print('Conexión interrumpida por cliente')
			quit()
		else:
			self.s.send(msg.encode())

if __name__ == '__main__':

	PORT = 12220
	client = ChatClient(PORT)

	while True:
	
		msg = input('... ')
		client.send_message(msg)

		ans = cliente.s.recv(1024)
		print('Servidor: ',ans.decode())