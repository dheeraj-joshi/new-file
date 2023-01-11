class rectangle:
    def area(self,lenght,breadth):
        self.length=lenght
        self.breadth=breadth
        print(lenght*breadth)
    def perimeter(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print(2*(length+breadth))
a=rectangle()
print("area")
a.area(20,40)
print()
print("perimeter")
a.perimeter(20,40)
        
