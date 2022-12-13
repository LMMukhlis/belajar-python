def triangleArea(base,height):
    area = 1/2*base*height
    print("Area of the triangle is",area,"cm2")

triangleArea(12,12)

def rectangleArea(length,width):
    area = length*width
    print("Area of the rectangle is",area,"cm2")

def rectanglePerimeter(length,width):
        perimeter = (length+width)*2
        print("the perimeter of the rectangle is",perimeter, "cm")

length = int(input("enter the length"))
width = int(input("enter the width"))

rectangleArea(length,width)
rectanglePerimeter(length,width)