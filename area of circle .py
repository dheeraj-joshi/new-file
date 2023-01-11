
'''7. Write a Python class named Circle constructed by a radius 
and two methods which will compute the area and the perimeter of a circle.'''

class Circle:
    def perimeter(self,pie,r):
        self.pie=pie
        self.r=r
        print(2*pie*r)
    def area(self,pie,r):
        self.pie=pie
        self.r=r 
        print(pie*r*r)
a=Circle()
print("area") 
a.area(3.14,7)
print()
print("perimeter")
a.perimeter(3.14,7)



        




















# class circle:
#         pie=3.14
#         r=7
#         print("perimeter of circle:",2*pie*r)
#         print("area of circle",pie*r*r)        
# a=circle()
