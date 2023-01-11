class Student:
    pass
class Student1(Student):
    pass
class Student3(Student1):
    def show(self,name,marks):
        self.name=name
        self.marks=marks
        print("name:",name," marks:",marks)
a=Student3()
a.show("dheeraj",23)
