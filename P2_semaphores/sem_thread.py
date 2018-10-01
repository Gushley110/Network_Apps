import threading
import time

a = list()
b = list()
zone = list()
sem = threading.Semaphore()

zone.append(a)
zone.append(b)

class Th_worker(threading.Thread):

	def __init__(self,th_id,th_name,char):
		threading.Thread.__init__(self)
		self.th_id = th_id
		self.th_name = 'Productor {}'.format(th_name)
		self.char = char

	def run(self):
		print('Starting {}'.format(self.th_name))
		sem.acquire()
		for i in range(20):
			print('{} [{}] = {}'.format(self.th_name,i,self.char))
			zone[0].append(self.char)
		sem.release()
		print('Exiting {}'.format(self.th_name))

class Th_consumer(threading.Thread):

	def __init__(self,th_id,th_name):
		threading.Thread.__init__(self)
		self.th_id = th_id
		self.th_name = 'Consumidor {}'.format(th_name)

	def run(self):
		print('Starting {}'.format(self.th_name))
		if zone[0][0] == 'a':
			for i in zone[0]:
				print('{} = {} '.format(self.th_name,i))
		if zone[0][1] == 'b':
			for i in zone[1]:
				print('{} = {} '.format(self.th_name,i))
		print('Exiting {}'.format(self.th_name))
			



# Create new threads
thread1 = Th_worker(0, "A",'a')
thread2 = Th_worker(1, "B",'b')
thread3 = Th_consumer(2,'A')
thread4 = Th_consumer(3,'B')

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()



