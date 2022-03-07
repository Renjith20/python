class rect:
    __length = ""
    __breadth = ""
    def __init__(self):
        self.__length = int(input("Enter the length: "))
        self.__breadth = int(input("Enter the breadth: "))
    def area(self):
        area = self.__length * self.__breadth
        return area
r1 = rect()
r2 = rect()

print("Area of rect 1 " , r1.area())
print("Area of rect2 " , r2.area())

if(r1.area() < r2.area()):
    print("Rectangle 2 is bigger")
else:
    print("rectangle 1 is bigger")
    