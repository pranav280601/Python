



def main():


	no1 = int(input("Enter 1st number:"))

	no2 = int(input("Enter 1st number:"))


	try:												
		
		print("Inside try")
		ans = no1/no2      


	except Exception as eobj:	
															
		print("Inside exception")
		
		print("Exception occurs",eobj)	

	else:	

		print("Inside else")

		print("Divsion is:",ans)

	finally:										

		print("De-Allocate all the resource")	



if __name__ == '__main__':
	main()
