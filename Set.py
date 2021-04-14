

def main():

	arr = {10,23.5,"Pranav",10}				

	print(type(arr))

	print(arr)

	print(len(arr))

	for i in arr:
		print(i)

	if "Pranav" in arr:
		print("It is present")	

	arr.add(20)
	
	print(arr)	

	arr.remove(20) 						 		

	print(arr)

	arr.discard(10)						

	print(arr)

			


if __name__ == '__main__':
		main()	
