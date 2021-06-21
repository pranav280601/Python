import sys


def Addition(x,y):
	return x+y


def main():
	if len(sys.argv)<3 or len(sys.argv)>3:
		print("Invalid number of arguments ")
		return

	ret = Addition(int(sys.argv[1]),int(sys.argv[2]))	
	print("Addition is:",ret)

if __name__ == "__main__" :
	main()	
