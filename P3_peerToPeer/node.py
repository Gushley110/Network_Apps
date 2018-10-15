import socket, threading
from libs.File_Manager import *

class P2P_Node():

    def __init__(self, port, host = 'localhost', keyword = '¬'):
        self.port = port
        self.host = host
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s_Clients = list()
        self.addr_Clients = list()
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
            if data == "FileList":
                pass
<<<<<<< HEAD
            elif data[0 : 14 ] == "filePetition: ":
=======
            else if data[0 : 14] == "filePetition: ":
>>>>>>> 6e2e1043b8b98c0685b34a28747b090f47bf8029
                fileName = data[ 14 :]
                bytesOfFile = self.getBytesOfFile(fileName)

            else:
                pass
            print('Cliente {}: '.format(str(addr[1])),data.decode())
            reply = input('... ')
            conn.sendall(reply.encode())

        print('Servidor cerrado')
        conn.close()
        quit()

    #lee un archivo en bytes
    def getBytesOfFile(self, fileName):

        fm = File_Manager(fileName, None)
        content = fm.get_text_bin()

        return content

    def createFileFromBytes(self, bytes, fileName):

        fm = File_Manager(None,fileName)
        fm.create_file_bin(bytes)

        return

    #Busca y devuelve un json con todos los archivos disponibles
    def getFileList(self):
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        j = json.dumps(onlyfiles)
        return j


    def start(self):
        print('[Esperando conexión ...]')
        while True:
            conn,addr = self.s.accept()
            threading.Thread(target=self.response, args=(conn, addr)).start()

    def startConnectionWithServer(self, ipServer, portConnection):
        #Usar semaforo para controlar el flujo en las variables globales
		self.s_Clients.append( socket.socket(socket.AF_INET, socket.SOCK_STREAM) )
		self.s_Clients[len(self.s_Clients) - 1].connect((self.host,self.port))
		self.addr_Clients ( self.s.getsockname() )
        print("Conexion exitosa con el servidor : " + self.addr_Clients[len(self.addr_Clients) - 1])


if __name__ == '__main__':
    PORT = 12220
    node = P2P_Node(PORT)
    threading.Thread( target=node.start, args=()).start()
    #Read from json and save it in ipNames
    #myIP have the information of the ip of the node
    for ip in ipNames:
        if ip != myIP :
            threading.Thread(target=node.startConnectionWithServer, args=(ip)).start()
