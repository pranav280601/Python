#name = lambda parameters : Funtion body



# named function
def Addition(n1,n2):
	return n1+n2


# using lambda function
Sum = lambda n1,n2 : n1+n2

def Fun(name):
	ret = name(10,20)
	print("Addition isss:",ret)

def main():
	x = int(input("Enter first number;"))
	y = int(input("Enter second number:"))
	ret = Addition(x,y)
	print("Addition is",ret)
	ret1 = Sum(x,y)
	print("Addition using lambda is:",ret1)
	Fun(Sum)
	Fun(Addition)


if __name__ == "__main__":
	main()