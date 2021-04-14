class Base1:


	def __init__(self):

		print("Inside Base1 Constructor")

	def fun(self):
		print("Inside Base1 fun")	



class Base2:

	def __init__(self):

		
		print("Inside Base2 Constructor")

	def fun(self):
		print("Inside Base2 fun")
			
	

class Derived(Base1,Base2):

	def __init__(self):

		Base1.__init__(self)
		Base2.__init__(self)

		print("Inside Derived Constructor")


def main():


	dobj = Derived()
	dob.fun()



if __name__ == '__main__':
	main()