class Tops():
    l=0
    b=0
    def __init__(self,*args):
        if len(args)==0:
            self.l=10
            self.b=10
        elif len(args)==1:
            self.l=args[0]
            self.b=args[0]
        elif len(args)==2:
            self.l=args[0]
            self.b=args[1]
    def area(self):
        print("Area Of Rectange Is : ",self.l*self.b)

t1=Tops()
t1.area()

t2=Tops(10)
t2.area()

t3=Tops(55,38)
t3.area()
