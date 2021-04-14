
import os
import threading
from time import sleep


def Thread1(no):
	print("Thread1 is created ")
	print("PID of Thread1 is",os.getpid())
	print("PID of parent of Thread1 is:",os.getppid())

	for i in range(no):
		sleep(1)
		print("Thread1",i)



def Thread2(no):
	print("Thread1 is created ")
	print("PID of thread1 is",os.getpid())
	print("PID of parent of Thread1 is:",os.getppid())

	for i in range(no):
		sleep(1)
		print("Thread2",i)


def main():

	print("Inside main process")
	print("PID of main process is:",os.getpid())
	print("PID of parent of main process is:",os.getppid())

	value = 10

	t1 = threading.Thread(target = Thread1 , args = (value,))
	t2 = threading.Thread(target = Thread2 , args = (value,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()
	

	print("End main process")




if __name__ == '__main__':
	main()