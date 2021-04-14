


class Base:

	def __init__(self):

		self.no1 = 10          
		self._no2 = 20			
		self.__no3 = 30			


	def fun(self):									
		print(self.no1,self._no2,self.__no3)

	def _fun(self):                                    
		print(self.no1,self._no2,self.__no3)	

	def __fun(self):										
		print(self.no1,self._no2,self.__no3)	


class Derived(Base):

	def __init__(self):
		Base.__init__(self)

	def gun(self):
		print(self.no1)
		print(self._no2)
		

		self.fun()
		self._fun()
		

def main():


	bobj = Base()
	print(bobj.no1)
	print(bobj._no2)
	                  
	bobj.fun()
	bobj._fun()
	                     

	dobj = Derived()
	dobj.gun()



if __name__ == '__main__':
	main()