class Student:

	def __init__(self,str,a,b,c):

		print("Inside constructor")

		self.name = str
		self.m1 =  a
		self.m2 =  b
		self.m3 =  c	
	
	def __eq__(self,other):

		print("Inside __eq__")

		if self.m1 == other.m1 and self.m2 == other.m2 and self.m3 == other.m3:
			return True

		else:
			False	


	def __gt__(self,other):

		print("Inside __gt__")

		if self.m1 >= other.m1 and self.m2 >= other.m2 and self.m3 >= other.m3:
			return True

		else:
			False	
		



def main():

	obj1 = Student("Pranav",60,50,60)

	obj2 = Student("XYZ",70,60,70)

	if obj1 == obj2:

		print("Both student are same")

	else:
		
		print("Both student are different")


	if obj1 > obj2:

		print("obj1 is greater")

	else:
		
		print("obj2 is greater")	
			




if __name__ == '__main__':
		main()	