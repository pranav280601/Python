
class Base:


	def __init__(self):

		self.i = 10
		self.j = 20

		print("Inside Base Constructor")


	def fun(self):
		print("Inside Base Fun")	


	
	def gun(self):
		print("Inside Base gun")	

class Derived(Base):

	def __init__(self):

		Base.__init__(self)

		self.x = 30
		self.y = 40

		print("Inside Derived Constructor")


	def Sun(self):
		print("Inside Derived sun")	


	
	def gun(self):                                 # Overriding
		print("Inside Derived gun")	


class Derived2(Derived):

	def __init__(self):

		Derived.__init__(self)

		self.a = 70
		self.b = 80



def main():

	bobj = Base()
	print(bobj.i)
	print(bobj.j)

	bobj.fun()
	bobj.gun()


	dobj = Derived()
	print(dobj.i)
	print(dobj.j)
	print(dobj.x)
	print(dobj.y)

	dobj.Sun()
	dobj.gun()


	d2obj = Derived2()
	print(d2obj.a)
	print(d2obj.b)



if __name__ == '__main__':
	main()