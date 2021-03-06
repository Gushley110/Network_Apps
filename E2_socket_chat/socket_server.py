import socket, threading

class ChatServer():

    def __init__(self, port, host = 'localhost', keyword = '¬'):
        self.port = port
        self.host = host
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.s.bind((self.host, self.port))
        except socket.error:
            print('Bind failed %s' % (socket.error))
            sys.exit()

        self.s.listen(5)

    def response(self, conn, addr):
        print('Client connected with ' + addr[0] + ':' + str(addr[1]))
        reply = ''
        while reply != '¬':
            data = conn.recv(1024)
            print('Cliente {}: '.format(str(addr[1])),data.decode())
            reply = input('... ')
            conn.sendall(reply.encode()) 
             
        print('Servidor cerrado')
        conn.close() 
        quit()

    def start(self):
        print('[Esperando conexión ...]')

        while True:
            conn,addr = self.s.accept()
            threading.Thread(target=self.response, args=(conn, addr)).start()



if __name__ == '__main__':
    PORT = 12220
    server = ChatServer(PORT)

    server.start()


   