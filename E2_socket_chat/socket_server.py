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
            print('Cliente: ',data.decode())
            reply = input('... ')
            conn.sendall(reply.encode()) 
             
        conn.close() # Close

    def start(self):
        print('[Esperando conexión ...]')

        while True:
            conn,addr = self.s.accept()
            threading.Thread(target=self.response, args=(conn, addr)).start()



if __name__ == '__main__':
    PORT = 12220
    server = ChatServer(PORT)
    # Run the chat server listening on PORT
    server.start()

    # Send a message to the chat server

   