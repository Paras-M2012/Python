'''
Class : it is a group of different types of variables and funcitons.

or

it is a group of objects.

object : it is an instance of class.

'''



class Student:

    def getData(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def putData(self):
        print("First Name : ",self.fname)
        print("Last Nmae : ",self.lname)
s1=Student()
s1.getData("Paras","Panchal")
s1.putData()

s2=Student()
s2.getData("Mantra","Panchal")
s2.putData()
