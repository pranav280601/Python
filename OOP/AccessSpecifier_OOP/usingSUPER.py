

class Base:
    def init(self):
        self.i = 10
        self.j = 20

    def fun(self):
        print("Base fun")

class Derived(Base):
    def init(self):
        Base.init(self)
        
        
        self.x = 30
        self.y = 40

    def gun(self):
        print("Derived gun")
        Base.fun(self)
        self.fun()         
        super().fun()       
        
        print(self.i)

dobj = Derived()
dobj.gun()
