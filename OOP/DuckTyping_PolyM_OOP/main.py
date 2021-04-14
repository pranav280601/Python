class C:

	def learnandCode(self):
		print("Learning C programming")


class Cpp:

	def learnandCode(self):
		print("Learning C++ programming")	

class Golang:

	def learnandCode(self):
		print("Learning Golang programming")	


class Demo:
	pass


class Programmer:

	def Coding(self,language):
		language.learnandCode()
	

def main():
				
	cobj = C()
	cpobj = Cpp()
	gobj = Golang()
	dobj = Demo()

	obj = Programmer()
	obj.Coding(cobj)
	obj.Coding(cpobj)
	obj.Coding(gobj)
	obj.Coding(dobj)


if __name__ == '__main__':
		main()	