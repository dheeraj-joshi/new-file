class Student:
    def show(self,name,marks):
        self.name=name
        self.marks=marks
        print(name,marks)
    def set_show(self,name,marks):
        self.name=name
        self.marks=marks
        print  (name,marks)
         
a=Student()
print("before seting the value:")
a.show("dheeraj",23)
print()
print("after setting the value:")
a.set_show("suraj",25)
