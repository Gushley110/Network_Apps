import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12219

exit_keyword = 'teamo'

s.connect((host, port))
print('Conectado a', host)

while True:
	z = input("Cliente: ")
	if z == exit_keyword:
		s.close()
		print('Ha terminado la conexion')
		quit()
	else:
		s.send(z.encode())

		print('[Esperando respuesta...]')
		print(s.recv(1024).decode())