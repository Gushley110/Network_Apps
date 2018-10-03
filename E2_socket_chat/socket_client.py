import socket

class ChatClient():

	def __init__(self,port,host = 'localhost', keyword = '¬'):
		self.port = port
		self.host = host
		self.keyword = keyword
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.host,self.port))
		self.addr = self.s.getsockname()

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
	print('[Cliente {}]'.format(client.addr[1]))

	while True:
	
		msg = input('... ')
		client.send_message(msg)

		ans = client.s.recv(1024)
		print('Servidor: ',ans.decode())