



def main():


	no1 = int(input("Enter 1st number:"))

	no2 = int(input("Enter 1st number:"))


	try:												# Also called as critical statement
		
		print("Inside try")
		ans = no1/no2      


	except Exception as eobj:	
														# Generic block (exception)	
		print("Inside exception")
		
		print("Exception occurs",eobj)	

	else:	

		print("Inside else")

		print("Divsion is:",ans)

	finally:											# Always runs 

		print("De-Allocate all the resource")	



if __name__ == '__main__':
	main()