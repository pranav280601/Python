


class Base1:


	def __init__(self):

		self.i = 10
		self.j = 20

		print("Inside Base1 Constructor")


	
class Base2:

	def __init__(self):

		
		self.x = 30
		self.y = 40

		print("Inside Base2 Constructor")


	

class Derived(Base1,Base2):

	def __init__(self):

		Base1.__init__(self)
		Base2.__init__(self)

		self.a = 70
		self.b = 80

		print("Inside Derived Constructor")


def main():

	#b1obj = Base1()
	#print(b1obj.i)
	#print(b1obj.j)

	

	#b2obj = Base2()
	#print(b2obj.i)
	#print(b2obj.j)
	#print(b2obj.x)
	#print(b2obj.y)

	

	dobj = Derived()
	print(dobj.i)
	print(dobj.j)
	print(dobj.x)
	print(dobj.y)
	print(dobj.a)
	print(dobj.b)



if __name__ == '__main__':
	main()