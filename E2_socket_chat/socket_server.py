import socket, threading

class ChatServer():

    def __init__(self, port, host = 'localhost', keyword = '¬'):
        self.port = port
        self.host = host
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.users = list()

        try:
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.s.bind((self.host, self.port))
        except socket.error:
            print('Bind failed %s' % (socket.error))
            sys.exit()

        self.s.listen(5)

    def response(self, conn, addr):
        print('Client connected with ' + addr[0] + ':' + str(addr[1]))
        while True:
            data = conn.recv(1024)
            print(data.decode())
            conn.sendall(reply) 
             
        conn.close() # Close

    def accept_connection(self):
        print('[Esperando conexión ...]')

        while True
            conn,addr = self.s.accept()
            threading.Thread(target=self.response, args=(conn, addr)).start()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12221

exit_keyword = 'teamo'

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
        msg = input('... ')
        q = 'Servidor: ' + msg
        if msg == exit_keyword:
            s.close()
            c.close()
            print('Ha terminado la conexion')
            quit()
        else:
            c.send(q.encode())
    