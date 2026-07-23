from abc import ABC,abstractmethod

'''
class RBI(ABC):
    def show(self):
        print("RBI Has been Declared That All Banks Have to Give Rate Of Interest To All Your Clients")

    @abstractmethod
    def roi(self):
        pass

class HDFC(RBI):
    def roi(self):
        print("Our Rate Of Interest is 7.5% Per Annum")

class SBI(RBI):
    def roi(self):
        print("Our Rate Of Interest is 5.5% Per Annum")

r1=HDFC()
r1.show()
r1.roi()

r2=SBI()
r2.roi()

'''

class RBI(ABC):
    @abstractmethod
    def roi(self,r):
        pass

class HDFC(RBI):
    def roi(self,r):
        print("Our Rate Of Interest is Per Annum : ",r)

class SBI(RBI):
    def roi(self,r):
        print("Our Rate Of Interest is Per Annum : ",r)

r1=HDFC()
r1.roi(5.7)

r2=SBI()
r2.roi(4.6)

