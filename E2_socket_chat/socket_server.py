import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12219

exit_keyword = 'teamo'

s.bind((host, port))

s.listen(5)
c = None

th_queue = list()
c_queue = list()
addr_queue = list()

def response(s,c,addr):
    print('Conectado desde', addr)
    print('[Esperando respuesta...]')
    print(c.recv(1024).decode())
    q = input("Servidor:")
    if q == exit_keyword:
        s.close()
        print('Ha terminado la conexion')
        quit()
    else:
        c.send(q.encode())
aux = 0

while True:
    print('[Esperando conexion...]')
    c, addr = s.accept()
    c_queue.append(c);
    addr_queue.append(addr);
    t = threading.Thread(target=response, name='nueva conexion' + str(aux), args=(s, c_queue[aux], addr[aux]))
    t.start()
    th_queue.append(t)
    aux += 1
    

    