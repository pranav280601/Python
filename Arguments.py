#positional arguments
def Student(Name,Roll,Addres,Marks):
	print("------------------------------------")
	
	print("Name is:",Name)
	print("Roll number is:",Roll)
	print("Addres is:",Addres)
	print("Marks is:",Marks)
	
	print("------------------------------------")



#Keyword argument
def Computer(Ram,Processor,Harddisk):
	print("Ram is:",Ram)
	print("Processor is:",Processor)
	print("Hard disk is:",Harddisk)
	print("------------------------------------")



#Default argument 
def CircleArea(Radius,Pi=3.14):
	print("value of pi is:",Pi)
	return Pi*Radius*Radius
	print("------------------------------------")


#Variable number of arguments
def fun(*Value):
	print("Number of arguments are:",len(Value))



def main():
	Student("Pranav",55,"Jalgaon",66)
	Computer(Processor = "i9", Ram = "8gb", Harddisk = "6gb")
	
	ret1 = CircleArea(10.25)
	print("Area of circle is:",ret1)

	ret2 = CircleArea(10.25,7.25)
	print("Area of circle is:",ret2)
	print("------------------------------------")


	fun(10,20,30)
	fun(45)
	fun(33,656,645,4654,5445)
	


if __name__ == "__main__":
	main()
