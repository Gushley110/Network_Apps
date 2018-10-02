import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12221

exit_keyword = 'teamo'

s.bind((host, port))

s.listen(5)
c = None

while True:
    if c is None:
        print('[Esperando conexion...]')
        c, addr = s.accept()
        print('Conectado desde', addr)
    else:
        print('[Esperando respuesta...]')
        print(c.recv(1024).decode())
        q = input("Servidor: ")
        if q == exit_keyword:
            s.close()
            print('Ha terminado la conexion')
            quit()
        else:
            c.send(q.encode())
    