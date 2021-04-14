

def DisplayW(value):
	x = 0
	while x<value:
		print("Jay Ganesh!!")
		x = x+1
	print("--------------------------------------")	



def DisplayF(value):                              #range(Start , End , Step)
	x = 0
	for x in range(0,value):
		print("Jay Ganesh!!")
	print("--------------------------------------")





def main():
	c = int(input("Enter the number of times you want to display the result:"))
	DisplayF(c)
	DisplayW(c)



if __name__ =="__main__":
	main()	