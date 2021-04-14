
from array import *

def main():

	arr = array('i',[10,20,30,40,110])		# i stands for int  # b for char     f - float   d - double

	print(type(arr))

	print("length is :",len(arr))

	print(arr)

	for i in range(len(arr)):
		print(arr[i])

	
	i = 0
	
	while i<len(arr):
		print(arr[i])
		i=i+1


if __name__ == '__main__':
		main()	