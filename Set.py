

def main():

	arr = {10,23.5,"Pranav",10}				# 10 - Duplication not allowed

	print(type(arr))

	print(arr)

	print(len(arr))

	for i in arr:
		print(i)

	if "Pranav" in arr:
		print("It is present")	

	arr.add(20)
	
	print(arr)	

	arr.remove(20) 						# arr.remove(120)  creates KeyError 		

	print(arr)

	arr.discard(10)						# arr.discard(120)   does not create exception   ignores and continue

	print(arr)

			


if __name__ == '__main__':
		main()	