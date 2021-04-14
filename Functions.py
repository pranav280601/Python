
def fun():
    print("\nFunction fun")


def gun(no):
    print("\nFunction gun",no)


def sun(no):
    print("\nFunction sun with parameter",no)
    return no+1


def AddSub(no1,no2):
    add = no1 + no2
    sub = no1 - no2
    return add,sub




def outer():
    def inner():
        print("inside inner")
    print("inside outer")
    inner()    
    


def mun():
    pass                         
    
    
def main():
    fun()
    gun(11)
    ret=sun(10)
    print("Returned value is:",ret)

    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))

    ret1,ret2=AddSub(x,y)
    print("Addition is:",ret1)
    print("Sub is:",ret2)


if __name__ == "__main__":
    main()
    outer()