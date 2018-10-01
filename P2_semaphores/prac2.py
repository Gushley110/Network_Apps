import threading
import time
import random
from libs.File_Manager import *

numberThreads = 4

class ThreadPool(object):

    def __init__(self):
        super(ThreadPool, self).__init__()
        self.lock = threading.Lock()
        self.directorio = list()
        self.mensajes = list()
        self.textMessages = ["Hola", "¿Como estas?", "How are you?", "Bye", "Adios"]

    def addNumber(self, newNumber): 
        f = File_Manager(None,'log.txt')
        # con el siguiente método te dá el número de hilo que está introduciendo datos threading.currentThread().getName()
        with self.lock:
            self.directorio.append(newNumber)
            f.append_text('=> #{}:{} [{}]'.format(newNumber,threading.currentThread().getName(),len(self.directorio) - 1))
            #print('Nueva entrada ',newNumber,' del hilo ', threading.currentThread().getName(), ' en la posicion ', len(self.directorio) - 1)

    def readNumbers(self):
        f = File_Manager(None,'directorio.txt')
        for i,n in enumerate(self.directorio):
            f.append_text('[{}] {}'.format(i,n))
        print("Imprimiendo directorio actual ", self.directorio)

    def addMessage(self):
        f = File_Manager(None,'mensajes.txt')
        with self.lock:
            msn = self.textMessages[random.randint(0, numberThreads - 1)]
            self.mensajes.append(msn)
            f.append_text('{}: {}'.format(threading.currentThread().getName(),msn))
            print('Nueva texto ',msn,' del hilo ', threading.currentThread().getName(), ' en la posicion ', len(self.mensajes) - 1)

    def readMessages(self):
        print("Imprimiendo directorio actual ", self.mensajes)




def writeNewNumber(semNumbers, pool, newNumber):
    print('Iniciando hilo ', threading.currentThread().getName())
    for i in range(1000):
        pool.addNumber(newNumber)
    semNumbers.release()
    pool.addMessage()
    semMessage.release()



def readDirectory(semNumbers, pool):
    print('Iniciando hilo ', threading.currentThread().getName())
    for x in range(numberThreads):
        semNumbers.acquire()
    pool.readNumbers()
    for x in range(numberThreads):
        semMessage.acquire()
    pool.readMessages()


f_directorio = File_Manager(None,'directorio.txt')
f_directorio.create_file('')
f_mensajes = File_Manager(None,'mensajes.txt')
f_mensajes.create_file('')
f_log = File_Manager(None,'log.txt')
f_log.create_file('')
pool = ThreadPool()
semNumbers = threading.Semaphore(0)
semMessage = threading.Semaphore(0)
for i in range(numberThreads):
    t = threading.Thread(target=writeNewNumber, name='thread_'+str(i), args=(semNumbers, pool, random.randint(100000000, 999999999)))
    t.start()
reader = threading.Thread(target=readDirectory, name='readerNumbers', args=(semNumbers, pool) )
reader.start()