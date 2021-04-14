
def Substraction(no1,no2):	
	print("Inside Substraction")
	return no1-no2	


def SubDecorator(func_name):
	
	print("Inside SubDecorator")
	
	def Updator(a,b): 						#Nested Function
		
		print("Inside Updator")

		if a < b: 							#First parameter is small
			temp = a						# a,b = b,a  (For swapping)
			a = b
			b = temp

		return func_name(a,b)	
	return Updator



def main():
	
	Sub = SubDecorator(Substraction)            #returns updator i.e Sub contains Updator

	x = int(input("Enter first number:"))
	y = int(input("Enter second number:"))
	
	ret = Sub(x,y)								# Call goes to updator(x,y)	
	print("Substraction is:",ret) 


if __name__ == '__main__':
	main()