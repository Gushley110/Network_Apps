import socket, threading
import json
from os import listdir
from os.path import isfile, join
from libs.File_Manager import *

class P2P_Node():

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
            if data == "FileList":
                pass
            else if data[0 : 14 ] == "filePetition: ":
                fileName = data[ 14 :]
                bytesOfFile = self.getBytesOfFile(fileName)

            else:

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



if __name__ == '__main__':
    PORT = 12220
    server = ChatServer(PORT)
    threading.Thread(target=server.start(), args=()).start()
    
    print("Codigo de cliente")  