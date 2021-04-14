def addition(value1,value2):    # : is necessary
	ret = value1 + value2
	return ret




def main():

	print("--------------------")
	x = int(input("enter first number:"))
	y = int(input("enter second number:"))	

	Ans = addition(x,y)

	print("Addition of {} ,{} is: {}".format(x,y,Ans))

	


if __name__ == '__main__':
	main()