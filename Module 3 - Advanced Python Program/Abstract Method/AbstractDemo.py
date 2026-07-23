from abc import ABC,abstractmethod

class Tops(ABC):
    def show(self):
        print("This Is Showing From TOPS")

    @abstractmethod
    def courses(self):
        pass

class TopsNikol(Tops):
    def courses(self):
        print("You Can Learn At Nikol Center All AI Related Courses")


t1=TopsNikol()
t1.show()
t1.courses()
