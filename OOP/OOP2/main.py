

class Demo:

	x= 10                                    # Class variable
	y=12


	def __init__(self):
		
		print("Inside constructor")
		
		self.i=34							#Instance Variable				
		self.j=45


	def __del__(self):                       #to remove allocated resources
		
		print("Inside Destructor")
	
	
	def fun(self):
		
		print("Inside fun")


	



def main():

	obj1 = Demo()                         #29 - 11 - 31 - 11 - 33 - 22 - 35 - 22 - 29(18) - 31(18)

	obj2 = Demo()

	obj1.fun()

	obj2.fun()

	del obj1
	del obj2

	#obj1.fun()




if __name__ == '__main__':
	main()
