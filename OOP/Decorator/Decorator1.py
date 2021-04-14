


def Substraction(no1,no2):
	
	return no1-no2	


def SubDecorator(func_name):

	return func_name(10,,5)



def main():
	
	

	ret = SubDecorator(Substraction)					# 19 --- 9 --- 4 --- 11 --- 19 --- 20	Also called as function chaining
	print("Substraction is:",ret) 


if __name__ == '__main__':
	main()