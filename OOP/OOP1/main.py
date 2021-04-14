


class Arithematic:                       
	
	value = 111                          



	def __init__(self,i,j):              
		
		print("Inside Cosntructor")

		
		self.no1=i                       

		self.no2=j				         


	def Add(self):                      
		return self.no1 + self.no2


	def Sub(self):                        
		return self.no1 - self.no2			



def main():

	

	print("value is",Arithematic.value)


	obj1 = Arithematic(42,11)             
	obj2 = Arithematic(90,32)            
	

	ret = obj1.Add()
	print("Addition is:",ret)
	ret = obj1.Sub()
	print("Substraction is:",ret)

	print("-------------------------------")

	ret = obj2.Add()
	print("Addition is:",ret)
	ret = obj2.Sub()
	print("Substraction is:",ret)


if __name__ == '__main__':
	main()