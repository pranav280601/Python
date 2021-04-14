i=0
a = 0
def Additon(b):
	global i
	global a
	if i < len(b):
		
		a = a +b[i]
		i = i+1
		Additon(b)
	return a	
	

def main():
	arr = []
	size = int(input("Enter the size:"))

	for a in range(size):
		arr.append(int(input()))

	print("Array is:",arr)
	
	ret = Additon(arr)	
	print("Output",ret)



if __name__ == '__main__':
		main()	
