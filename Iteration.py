
#Sequence approach
def Start():
	print("Jay Ganesh!!")
	print("Jay Ganesh!!")
	print("Jay Ganesh!!")
	print("Jay Ganesh!!")
	print("Jay Ganesh!!")
	print("--------------------------------------")



#Iterative approach

def Start1():
	x = 0
	while x<5:
		print("Jay Ganesh!!")
		x = x+1
	print("--------------------------------------")	



#Iterative approach

def Start2(value):
	a = 0
	while a<value:
		print("Jay Ganesh!!")
		a = a+1
	print("--------------------------------------")




def Start3(value,message):
	a = 0
	while a<value:
		print(message)
		a = a+1
	print("--------------------------------------")


def main():
	c = int(input("Enter the number of times you want to display the result:"))
	v = input("Enter the message you want to display:")
	Start()
	Start1()
	Start2(c)
	Start3(c,v)


if __name__ =="__main__":
	main()	